import httpx
from lib import cmdLine,getModule,Banner,Option
import importlib
import threading,time
def run():
    module_path = "Script"
    module_list = getModule.get_module(module_path) #获取payload
    module_list = [m.strip() for m in module_list if m.strip() != '']   ##去除可能导致module为空，导致导入包错误的情况

    args = cmdLine.get_options()
    # path = cmdLine.get_options()    #获取args参数

    path = Option.get_target(args)
    single_module = Option.get_single_module(args)  #获取单个module，用于指定module运行
    single_module = str(single_module)
    threads = []
    for module in module_list:
        #指定单个module运行，注意根据poc命名的第一个下划线前面的名称即可
        if single_module !='None' and single_module in module:
            new_module = module_path + '.' + module
            print("当前加载的module：" + new_module)
            module_object_m = importlib.import_module(new_module)         #动态注册模块
            for target in path:
                t = threading.Thread(target=module_object_m.poc, args=(target,))
                t.start()
                threads.append(t)

        #不指定module运行
        if single_module == 'None':
            new_module = module_path + '.' + module
            print("当前加载的module：" + new_module)
            module_object = importlib.import_module(new_module)         #动态注册模块
            for target in path:
                t = threading.Thread(target=module_object.poc, args=(target,))
                t.start()
                threads.append(t)

if __name__ == "__main__":
    Banner.banner()
    run()




