# import asyncio
#
# def getfile():
#     for i in range(pow(10,10)):
#         print(i)
#
# @asyncio.coroutine
# def hello1():
#     print("hello asyncio")
#     r=getfile()
#     print("hello again")
#
#
# loop=asyncio.get_event_loop()
# loop.run_until_complete(hello1())
# loop.close()

import  threading
# import asyncio
#
# def hello():
#     print("hello asyncio %s" % threading.current_thread())
#     yield from asyncio.sleep(1)
#     print("hello again %s " % threading.current_thread())
#
# loop=asyncio.get_event_loop()
# tasks=[hello(),hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


# import asyncio
#
# def hello_world(loop):
#     while 1:
#         try:
#             print("死循环")
#         except KeyboardInterrupt:
#             print("程序被中断")
#             break
#     print("loop before")
#     loop.stop()
#     print("loop agter")
#
# loop = asyncio.get_event_loop()
#
# # Schedule a call to hello_world()
# loop.call_soon(hello_world, loop)
#
# # Blocking call interrupted by loop.stop()
# loop.run_forever()
# loop.close()

#
# import asyncio
# import time
# @asyncio.coroutine
# def getfile():
#     for i in range(100):
#         print(i)
#         time.sleep(1)
#
# @asyncio.coroutine
# def hello():
#     for x in range(100):
#         print("hello asyncio")
#         print("hello again")
#
# tasks=[hello(),getfile()]
# loop=asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
    
# import asyncio
# # from socket import socketpair
# from asyncio.windows_utils import socketpair
#
# rsock,wsock=socketpair()
# loop=asyncio.get_event_loop()
#
# def reader():
#     data=rsock.recv(100)
#     print("Received",data.decode())
#     loop.remove_reader(rsock)
#     loop.stop()
#
# loop.add_reader(rsock,reader())
# loop.call_soon(wsock.send(),"aaa".encode())
#
# loop.run_forever()
#
# wsock.close()
# wsock.close()
# loop.close()
#

# import asyncio
#
# def curl(host):
#     print("下载 %s" % host )
#     conn=asyncio.open_connection(host,80)
#     r,w=yield from conn
#     headers='GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     w.write(headers.encode('utf-8'))
#     yield  from w.drain()
#     while 1:
#         line=yield  from r.readline()
#         if line ==b'\r\n':
#             break
#         print("header",(host,line.decode("utf-8").rstrip()))
#     w.close()
#
# loop=asyncio.get_event_loop()
# tasks=[curl(host) for host in ["www.baidu.com","www.qq.com","mail.126.com"]]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
#
#
    
    
    
    
    
    
    
    

