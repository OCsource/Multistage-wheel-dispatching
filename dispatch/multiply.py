import queue,time,os,threading

# 线程1，多级轮转函数
class applyRound(threading.Thread):
    def __init__(self,hasSomeProcessCome,allTime,other):
        threading.Thread.__init__(self)
        self.hasSomeProcessCome = hasSomeProcessCome
        self.allTime = allTime
        self.other = other
        # 创建已有的线程字典
        self.dictP = {}
        # 创建多级队列
        self.runProcess = [[],[],[]]
        # 创建将要准备队列
        self.readyProcess = queue.Queue()
        # 创建时间对应的线程列表
        self.timeProcesses = []
        # 正在运行的线程
        self.doingProcess = [None, 0]
        # 队列中的所有线程按运行顺序排列
        self.sequenceProcess = []

        # 其他用于与主函数交互的值
        self.yData = 0
        self.yData2 = 0
        self.mainLine = [self.other.QLineEdit,self.other.QLineEdit_1,self.other.QLineEdit_2]

    # 写入log
    def writeLog(self,sss):
        path = './resource/runLog.txt'
        if sss != '':
            fin = open(path, "a", encoding='utf8')
            fin.write(sss + '\n')
            fin.close()

    # 运行多级轮转
    def run(self):

        if os.path.getsize('./resource/runLog.txt'):
            with open('./resource/runLog.txt', 'w') as f:
                f.truncate()

        while True:
            # sT = time.time()
            tempList = []  # 存放本次时间内加入的线程
            self.sequenceProcess = []
            self.yData2 = 0
            # 遍历准备队列，将时间到了的线程加载到一级队列中
            for i in self.dictP:
                if self.dictP[i].startTime <= self.allTime:
                    print('线程%s,加入第一队列！-- 时间%s' % (self.dictP[i].id, self.allTime))
                    # self.writeLog('线程%s,加入第一队列！-- 时间%s' % (self.dictP[i].id, self.allTime))
                    self.other.textList.append('线程%s,加入第一队列！-- 时间%s' % (self.dictP[i].id, self.allTime))
                    self.runProcess[0].append(self.dictP[i])
                    tempList.append(i)
            # 将上面加入的线程从字典中pop出去
            for p in tempList:
                self.dictP.pop(p)
            
            # 如果有队列加入，则将运行中的线程加入到队尾
            if self.hasSomeProcessCome == True and self.doingProcess[0] != None and self.doingProcess[1] != 0:
                print('新的线程进入，正在运行的线程%s的靠后！-- 时间%s'%(self.doingProcess[0].id, self.allTime))
                # self.writeLog('新的线程进入，正在运行的线程%s的靠后！-- 时间%s'%(self.doingProcess[0].id, self.allTime))
                self.other.textList.append('新的线程进入，正在运行的线程%s的靠后！-- 时间%s'%(self.doingProcess[0].id, self.allTime))
                self.runProcess[self.doingProcess[1]].remove(self.doingProcess[0])
                self.runProcess[self.doingProcess[1]].append(self.doingProcess[0])
                self.other.x.append(self.allTime)
                self.other.y.append(self.runProcess[0][0].id)

            # 更新顺序队列
            for i in range(len(self.runProcess)):
                temp = [str(self.runProcess[i][j].id) for j in range(len(self.runProcess[i]))]
                # print(temp)
                self.mainLine[i].setText(','.join(temp))
                self.sequenceProcess += self.runProcess[i]

            # 如果没有正在执行的process退出
            if self.sequenceProcess == [] and len(self.dictP) == 0:
                print('总运行时间为：%s'%(self.allTime))
                # self.writeLog('总运行时间为：%s'%(self.allTime))
                self.other.textList.append('总运行时间为：%s'%(self.allTime))
                self.other.on_stop()
                return False

            if len(self.runProcess[0]) != 0:     # 遍历一级队列执行任务
                self.runInList(0,10)
            elif len(self.runProcess[1]) != 0:   # 遍历二级队列执行任务
                self.runInList(1,100)
            elif len(self.runProcess[2]) != 0:   # 遍历三级队列执行任务
                self.runInList(2,1000)

            self.allTime += 1
            self.hasSomeProcessCome = False
            self.other.x.append(self.allTime)
            self.other.y.append(self.yData)
            if self.yData2:
                self.other.x.append(self.allTime)
                self.other.y.append(self.yData2)
            print('现在是%s，休眠一秒钟....'%(self.allTime))
            time.sleep(1)
            # print(time.time()-sT)

    # 在队列中运行
    def runInList(self,i, runTime):
        self.doingProcess[0] = self.runProcess[i][0]
        self.doingProcess[1] = i
        self.doingProcess[0].serverTime -= 1
        self.doingProcess[0].getTime += 1
        self.yData = self.doingProcess[0].id
        if self.doingProcess[0].serverTime == 0:
            print('线程%s:运行完毕，结束！-- 时间:%s' % (self.doingProcess[0].id, self.allTime + 1))
            # self.writeLog('线程%s:运行完毕，结束！-- 时间:%s' % (self.doingProcess[0].id, self.allTime + 1))
            self.other.textList.append('线程%s:运行完毕，结束！-- 时间:%s' % (self.doingProcess[0].id, self.allTime + 1))
            self.doingProcess[0].endTime = self.allTime
            self.runProcess[i].remove(self.doingProcess[0])
            self.sequenceProcess.remove(self.doingProcess[0])
            if self.sequenceProcess != []:
                self.yData2 = self.sequenceProcess[0].id
            else:
                self.yData2 = self.other.y[-1]
            self.doingProcess[0] = None
        elif self.doingProcess[0].getTime == runTime:
            print('线程%s:时间片运行完了，进入下一个队列！-- 时间:%s' % (self.doingProcess[0].id, self.allTime + 1))
            # self.writeLog('线程%s:时间片运行完了，进入下一个队列！-- 时间:%s' % (self.doingProcess[0].id, self.allTime + 1))
            self.other.textList.append('线程%s:时间片运行完了，进入下一个队列！-- 时间:%s' % (self.doingProcess[0].id, self.allTime + 1))
            self.doingProcess[0].getTime = 0
            self.runProcess[i].remove(self.doingProcess[0])
            j = i if i == len(self.runProcess) - 1 else i + 1
            self.runProcess[j].append(self.doingProcess[0])
            self.sequenceProcess = []
            for i in range(len(self.runProcess)):
                self.sequenceProcess += self.runProcess[i]
            if self.sequenceProcess != []:
                self.yData2 = self.sequenceProcess[0].id
            else:
                self.yData2 = self.other.y[-1]

# if __name__ == '__main__':
#     self.dictP = applyRound.readDispatch('./resource/dispatch.txt')
#     applyRound.main(self.dictP)