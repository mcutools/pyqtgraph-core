# -*- coding: utf-8 -*-
from lib.modules.Module import *
from ProtocolRunnerTemplate import *
from PyQt4 import QtGui, QtCore
from lib.util.DirTreeModel import *
from lib.util.configfile import *
from lib.util.advancedTypes import OrderedDict
import time

class ProtocolRunner(Module, QtCore.QObject):
    def __init__(self, manager, name, config):
        Module.__init__(self, manager, name, config)
        QtCore.QObject.__init__(self)
        self.devListItems = {}
        self.seqListItems = OrderedDict()  ## Looks like {(device, param): listItem, ...}
        self.docks = {}
        self.deleteState = 0
        self.ui = Ui_MainWindow()
        self.win = QtGui.QMainWindow()
        self.ui.setupUi(self.win)
        
        self.protocolList = DirTreeModel(self.config['globalDir'])
        self.ui.protocolList.setModel(self.protocolList)
        
        self.currentProtocol = None   ## pointer to current protocol object
        
        #self.updateDeviceList()
        
        self.newProtocol()
        
        self.taskThread = TaskThread(self)
        
        QtCore.QObject.connect(self.ui.newProtocolBtn, QtCore.SIGNAL('clicked()'), self.newProtocol)
        QtCore.QObject.connect(self.ui.saveProtocolBtn, QtCore.SIGNAL('clicked()'), self.saveProtocol)
        QtCore.QObject.connect(self.ui.loadProtocolBtn, QtCore.SIGNAL('clicked()'), self.loadProtocol)
        QtCore.QObject.connect(self.ui.saveAsProtocolBtn, QtCore.SIGNAL('clicked()'), self.saveProtocolAs)
        QtCore.QObject.connect(self.ui.deleteProtocolBtn, QtCore.SIGNAL('clicked()'), self.deleteProtocol)
        QtCore.QObject.connect(self.ui.testSingleBtn, QtCore.SIGNAL('clicked()'), self.testSingle)
        QtCore.QObject.connect(self.ui.runProtocolBtn, QtCore.SIGNAL('clicked()'), self.runSingle)
        QtCore.QObject.connect(self.ui.deviceList, QtCore.SIGNAL('itemClicked(QListWidgetItem*)'), self.deviceItemChanged)
        QtCore.QObject.connect(self.ui.protoDurationSpin, QtCore.SIGNAL('editingFinished()'), self.protParamsChanged)
        QtCore.QObject.connect(self.ui.protocolList, QtCore.SIGNAL('doubleClicked(const QModelIndex &)'), self.loadProtocol)
        QtCore.QObject.connect(self.ui.protocolList, QtCore.SIGNAL('clicked(const QModelIndex &)'), self.protoListClicked)
        QtCore.QObject.connect(self.protocolList, QtCore.SIGNAL('fileRenamed(PyQt_PyObject, PyQt_PyObject)'), self.fileRenamed)
        QtCore.QObject.connect(self.taskThread, QtCore.SIGNAL('finished()'), self.taskThreadStopped)
        QtCore.QObject.connect(self.taskThread, QtCore.SIGNAL('newFrame(PyQt_PyObject)'), self.handleFrame)
        
        self.win.show()
        
    def getDevice(self, dev):
        try:
            item = self.ui.deviceList.findItems(dev, QtCore.Qt.MatchExactly)[0]
        except:
            raise Exception('Requested device %s does not exist!' % dev)
        item.setCheckState(QtCore.Qt.Checked)
        self.deviceItemChanged(item)
        #self.docks[dev].show()
        return self.docks[dev].widget()
        
    def getParam(self, param):
        return self.currentProtocol.conf[param]
        
    def updateDeviceList(self, protocol=None):
        """Read the list of devices from the device manager"""
        devList = self.manager.listDevices()
        
        if protocol is not None:
            protList = protocol.conf['devices'].keys()
        elif self.currentProtocol is not None:
            protList = self.currentProtocol.conf['devices'].keys()
        else:
            protList = []
            
        ## Remove all devices that do not exist and are not referenced by the protocol
        rem = []
        for d in self.devListItems:
            if d not in devList and d not in protList:
                #print "    ", d
                self.ui.deviceList.takeItem(self.ui.deviceList.row(self.devListItems[d]))
                rem.append(d)
        for d in rem:
            del self.devListItems[d]
                
        ## Add all devices that exist in the current system
        for d in devList:
            if d not in self.devListItems:
                self.devListItems[d] = QtGui.QListWidgetItem(d, self.ui.deviceList)
            self.devListItems[d].setForeground(QtGui.QBrush(QtGui.QColor(0,0,0)))
            
            
        ## Add all devices that are referenced by the protocol but do not exist
        
        for d in protList:
            if d not in self.devListItems:
                self.devListItems[d] = QtGui.QListWidgetItem(d, self.ui.deviceList)
                self.devListItems[d].setForeground(QtGui.QBrush(QtGui.QColor(150,0,0)))
            
        ## Make sure flags and checkState are correct for all items
        for d in self.devListItems:
            self.devListItems[d].setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
            if d in protList:
                self.devListItems[d].setCheckState(QtCore.Qt.Checked)
            else:
                self.devListItems[d].setCheckState(QtCore.Qt.Unchecked)
                
    def protoListClicked(self, ind):
        ## Check to see if the selection has changed
        sel = list(self.ui.protocolList.selectedIndexes())
        if len(sel) == 1:
            self.ui.deleteProtocolBtn.setEnabled(True)
        else:
            self.ui.deleteProtocolBtn.setEnabled(False)
        self.resetDeleteState()
            
    def fileRenamed(self, fn1, fn2):
        ## A file was renamed, we might need to act on this change..
        if fn1 == self.currentProtocol.fileName:
            self.currentProtocol.fileName = fn2
            pn = fn2.replace(self.protocolList.baseDir, '')
            self.ui.currentProtocolLabel.setText(pn)
            return
        if os.path.isdir(fn2) and fn1 in self.currentProtocol.fileName:
            self.currentProtocol.fileName = self.currentProtocol.fileName.replace(fn1, fn2)
            pn = self.currentProtocol.fileName.replace(self.protocolList.baseDir, '')
            self.ui.currentProtocolLabel.setText(pn)
            return
            
    def hideDock(self, dev):
        self.docks[dev].hide()
        for i in self.seqListItems:
            if i[0] == dev
                self.seqListItems[i].hide()
        
    def showDock(self, dev):
        self.docks[dev].hide()
        for i in self.seqListItems:
            if i[0] == dev
                self.seqListItems[i].show()
        
    def updateSeqParams(self, dev):
        #if l not in self.seqListItems:
            #self.seqListItems[dev] = []
        #l = self.seqListItems[dev]
        params = self.docks[dev].widget().listSequence()
        
        ## Add new sequence parameters, update old ones
        for p in params:
            item = (dev, p)
            if item not in self.seqListItems:
                self.seqListItems[item] = QListWidgetItem('%s.%s' % (dev, p))
                self.ui.sequenceParamList.addItem(self.seqListItems[item])
            self.seqListItems[item].setData(params[p])
            
        ## remove non-existent sequence parameters
        for key in self.seqListItems:
            if key[0] == dev and key[1] not in params:
                self.ui.sequenceParamList.removeItem(self.seqListItems[key])
                del self.seqListItems[key]
        
    def updateDocks(self, protocol = None):
        if protocol is None:
            protocol = self.currentProtocol
        
        ## (un)hide docks as needed
        for d in self.docks:
            if self.docks[d] is None:
                continue
            if d not in protocol.enabledDevices():
                self.hideDock(d)
            else:
                self.showDock(d)
            
        ## Create docks that don't exist
        for d in protocol.enabledDevices():
            if d not in self.docks:
                if d not in self.manager.listDevices():
                    continue
                self.docks[d] = None  ## Instantiate to prevent endless loops!
                
                dev = self.manager.getDevice(d)
                dw = dev.protocolInterface(self)
                dock = QtGui.QDockWidget(d)
                dock.setFeatures(dock.AllDockWidgetFeatures)
                dock.setObjectName(d)
                dock.setWidget(dw)
                dock.setAutoFillBackground(True)
                
                self.docks[d] = dock
                self.win.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)
                
                self.updateSeqParams(d)
        
    def deviceItemChanged(self, item):
        if item.checkState() == QtCore.Qt.Unchecked:
            self.currentProtocol.removeDevice(str(item.text()))
        else:
            self.currentProtocol.addDevice(str(item.text()))
        self.updateDocks()
        
    def clearDocks(self):
        for d in self.docks:
            self.win.removeDockWidget(self.docks[d])
        self.docks = {}
        self.ui.sequenceParamList.clear()
        self.seqListItems = OrderedDict()
                
        
    def closeProtocol(self):
        ## Remove all docks
        self.clearDocks()
        
        ## Clear sequence list
        self.ui.sequenceList.clearItems()
        
    def protParamsChanged(self):
        self.currentProtocol.conf['duration'] = self.ui.protoDurationSpin.value()
        self.currentProtocol.conf['continuous'] = self.ui.protoContinuousCheck.isChecked()
        #self.currentIsModified(True)
        
    #def currentIsModified(self, v):
        ### Inform the module whether the current protocol is modified from its stored state
        #self.currentProtocol.modified = v
        #if (not v) or (self.currentProtocol.fileName is not None):
            #self.ui.saveProtocolBtn.setEnabled(v)
        
    def newProtocol(self):
        ## Remove all docks
        self.clearDocks()
        
        ## Create new empty protocol object
        self.currentProtocol = Protocol()
        
        ## Clear extra devices in dev list
        self.updateDeviceList()
        
        self.updateProtParams()
        
        ## Clear sequence parameters, disable sequence dock
        
        self.ui.currentProtocolLabel.setText('[ new ]')
        
        self.ui.saveProtocolBtn.setEnabled(False)
        #self.currentIsModified(False)
    
    def updateProtParams(self, prot=None):
        if prot is None:
            prot = self.currentProtocol
        self.ui.protoDurationSpin.setValue(prot.conf['duration'])
        if prot.conf['continuous']:
            self.ui.protoContinuousCheck.setCheckState(QtCore.Qt.Checked)
        else:
            self.ui.protoContinuousCheck.setCheckState(QtCore.Qt.Unchecked)
    
    def getSelectedFileName(self):
        sel = list(self.ui.protocolList.selectedIndexes())
        if len(sel) == 1:
            index = sel[0]
        else:
            raise Exception("Can not load--%d items selected" % len(sel))
        return self.protocolList.getFileName(index)
    
    def loadProtocol(self, index=None):
        ## Determine selected item
        if index is None:
            sel = list(self.ui.protocolList.selectedIndexes())
            if len(sel) == 1:
                index = sel[0]
            else:
                raise Exception("Can not load--%d items selected" % len(sel))
            
        fn = self.protocolList.getFileName(index)
        
        ## Create protocol object from requested file
        prot = Protocol(fileName=fn)
        
        ## Remove all docks
        self.clearDocks()
        
        ## Update protocol parameters
        self.updateProtParams(prot)
        
        ## update dev list
        self.updateDeviceList(prot)
        
        ## Update sequence parameters, dis/enable sequence dock
        
        ## Create new docks
        self.updateDocks(prot)
        
        ## Configure docks
        for d in prot.conf['devices']:
            self.docks[d].widget().restoreState(prot.conf['devices'][d])
            
        ## Configure dock positions
        if 'winState' in prot.conf:
            self.win.restoreState(QtCore.QByteArray.fromPercentEncoding(prot.conf['winState']))
            
        pn = fn.replace(self.protocolList.baseDir, '')
        self.ui.currentProtocolLabel.setText(pn)
        self.currentProtocol = prot
        self.ui.saveProtocolBtn.setEnabled(True)
        #self.currentIsModified(False)
    
    def saveProtocol(self, fileName=None):
        ## store window state
        ws = str(self.win.saveState().toPercentEncoding())
        self.currentProtocol.conf['winState'] = ws
        
        ## store individual dock states
        for d in self.docks:
            if self.currentProtocol.deviceEnabled(d):
                self.currentProtocol.conf['devices'][d] = self.docks[d].widget().saveState()
        
        ## Write protocol config to file
        self.currentProtocol.write(fileName)
        #self.currentIsModified(False)
        
        ## refresh protocol list
        self.protocolList.clearCache()
    
    def saveProtocolAs(self):
        ## Decide on new file name
        if self.currentProtocol.fileName is not None:
            baseFile = self.currentProtocol.fileName
        else:
            baseFile = os.path.join(self.protocolList.baseDir, 'protocol')
            
        c = 2
        newFile = None
        while True:
            newFile = baseFile + '_%02d' % c
            if not os.path.exists(newFile):
                break
            c += 1
            
        ## write
        self.saveProtocol(newFile)
        
        
        ## Start editing new file name
        index = self.protocolList.findIndex(newFile)
        #self.ui.protocolList.update(index)
        self.ui.protocolList.edit(index)
        
        pn = newFile.replace(self.protocolList.baseDir, '')
        self.ui.currentProtocolLabel.setText(pn)
        self.ui.saveProtocolBtn.setEnabled(True)
        #self.currentIsModified(False)
    
    def deleteProtocol(self):
        ## Delete button must be clicked twice.
        if self.deleteState == 0:
            self.ui.deleteProtocolBtn.setText('Really?')
            self.deleteState = 1
        elif self.deleteState == 1:
            try:
                fn = self.getSelectedFileName()
                os.remove(fn)
                self.protocolList.clearCache()
            except:
                sys.excepthook(*sys.exc_info())
                return
            finally:
                self.resetDeleteState()
    
    def resetDeleteState(self):
        self.deleteState = 0
        self.ui.deleteProtocolBtn.setText('Delete')
    
    def testSingle(self):
        self.runSingle(store=False)
    
    def runSingle(self, store=True):
        ## Disable all start buttons
        self.enableStartBtns(False)
        
        ## Generate executable conf from protocol object
        prot = {'protocol': {
            'duration': self.currentProtocol.conf['duration'], 
            'storeData': store,
            'mode': 'single',
            'name': self.currentProtocol.fileName,
        }}
        
        for d in self.currentProtocol.conf['devices']:
            if self.currentProtocol.deviceEnabled(d):
                prot[d] = self.docks[d].widget().generateProtocol()
        
        self.emit(QtCore.SIGNAL('protocolStarted()'))
        self.taskThread.startProtocol(prot)
        
   
    def testSequence(self):
        self.runSequence(store=False)
       
    def runSequence(self):
        pass
    
    def enableStartBtns(self, v):
        btns = [self.ui.testSingleBtn, self.ui.runProtocolBtn, self.ui.testSequenceBtn, self.ui.runSequenceBtn]
        for b in btns:
            b.setEnabled(v)
            
    def taskThreadStopped(self):
        self.enableStartBtns(True)
    
    def handleFrame(self, frame):
        print "Got frame"
        dataManager = None
        ## Should this data be stored?
        if frame['cmd']['protocol']['storeData']:
            ## Create directory for storing 
            pass
            ## Store protocol command and parameter details
        ## Request each device handles its own data
        for d in frame['result']:
            if d != 'protocol':
                self.docks[d].widget().handleResult(frame['result'][d], dataManager)
    
class Protocol:
    def __init__(self, fileName=None):
        
        if fileName is not None:
            self.name = os.path.split(fileName)[1]
            self.fileName = fileName
            self.conf = readConfigFile(fileName)
            self.enabled = self.conf['devices'].keys()
        else:
            self.fileName = None
            self.name = None
            self.conf = {'devices': {}, 'duration': 0.2, 'continuous': False}
            self.enabled = []
        
    def generateProtocol(self, **args):
        """Generate the configuration data that will execute this protocol"""
        
        pass
    
    def deviceEnabled(self, dev):
        return dev in self.enabled
        
        
    def write(self, fileName=None):
        conf = self.conf.copy()
        
        ## Remove unused devices before writing
        rem = [d for d in conf['devices'] if not self.deviceEnabled(d)]
        for d in rem:
            del conf['devices'][d]
                
        if fileName is None:
            if self.fileName is None:
                raise Exception("Can not write protocol--no file name specified")
            fileName = self.fileName
        self.fileName = fileName
        writeConfigFile(conf, fileName)
    
    def enabledDevices(self):
        return self.enabled[:]
        
    def removeDevice(self, dev):
        if dev in self.enabled:
            self.enabled.remove(dev)
        
    def addDevice(self, dev):
        if dev not in self.conf['devices']:
            self.conf['devices'][dev] = {}
        if dev not in self.enabled:
            self.enabled.append(dev)
            
            
class TaskThread(QtCore.QThread):
    def __init__(self, ui):
        QtCore.QThread.__init__(self)
        self.ui = ui
        self.dm = self.ui.manager
        self.lock = QtCore.QMutex(QtCore.QMutex.Recursive)
        self.stopThread = True
                
    def startProtocol(self, protocol, paramSpace=None):
        l = QtCore.QMutexLocker(self.lock)
        if self.isRunning():
            raise Exception("Already running another protocol")
        self.protocol = protocol
        self.paramSpace = paramSpace
        self.lastRunTime = None
        self.start()
    
                
    def run(self):
        try:
            l = QtCore.QMutexLocker(self.lock)
            self.stopThread = False
            l.unlock()
            
            if self.paramSpace is None:
                result = self.runOnce()
            else:
                result = runSequence(self.runOnce, self.paramSpace, self.paramSpace.keys(), passHash=True)
            
        except:
            print "Error in protocol thread, exiting."
            sys.excepthook(*sys.exc_info())
        #finally:
            #self.emit(QtCore.SIGNAL("protocolFinished()"))
                    
    def runOnce(self, params=None):
        ## Select correct command to execute
        cmd = self.protocol
        if params is not None:
            for p in params:
                cmd = cmd[p]
                
        ## Todo: wait before starting if we've already run too recently
        while (self.lastRunTime is not None) and (time.clock() < self.lastRunTime + cmd['protocol']['cycleTime']):
            time.sleep(1e-3)
        
        ## Run
        #print "Create task:"
        #print cmd
        task = self.dm.createTask(cmd)
        self.lastRunTime = time.clock()
        task.execute()
            
        ## wait for finish, watch for abort requests
        while True:
            if task.isDone():
                break
            #if self.abort:
                #task.abort()
                #print "Protocol run aborted by user"
                #return
            ## Abort if protocol is taking too long
            #if time.clock() >= (self.lastRunTime+(cmd['protocol']['duration']+0.2)):
                #print "Protocol run aborted--timeout"
                #task.abort()
                #return
            time.sleep(100e-6)
        
        result = task.getResult()
        frame = {'params': params, 'cmd': cmd, 'result': result}
        self.emit(QtCore.SIGNAL('newFrame(PyQt_PyObject)'), frame)
        return result
                    
    def stop(self, block=False):
        l = QtCore.QMutexLocker(self.lock)
        self.stopThread = True
        l.unlock()
        if block:
            self.wait()