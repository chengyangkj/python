from gevent import monkey
import gevent
import random
import time

# 有耗时操作时需要
monkey.patch_all()  # 将程序中用到的耗时操作的代码，换为gevent中自己实现的模块

def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name, i)
        time.sleep(random.random())
#g1 = gevent.spawn(coroutine_work,"work1")
#g2 = gevent.spawn(coroutine_work,"work2")
#g1.join()
#g2.join()
#上面四行代码等同于下面代码
gevent.joinall([
        gevent.spawn(coroutine_work, "work1"),
        gevent.spawn(coroutine_work, "work2")
])
