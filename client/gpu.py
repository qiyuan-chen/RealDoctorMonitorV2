import time
import os



def get_gpu_usage_info():
    # 得到GPU的使用情况

    # 只精确到秒，转化为字符串
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    gpu_info = os.popen(
        "nvidia-smi --query-gpu=gpu_name,memory.total,memory.used --format=csv,noheader,nounits").read().strip().split("\n")
    process_info = os.popen(
        "nvidia-smi pmon -c 1").read().strip().split("\n")[2:]
    utilization_info = os.popen(
        "nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits").read().strip().split("\n")

    result_list = []
    for line in process_info:
        # 对于每张显卡，获取其对应的进程信息
        parts = line.split()
        if len(parts) >= 4:
            gpu_id, pid = parts[0].strip(), parts[1].strip()
            if pid != '-':
                user = os.popen(f"ps -o user= -p {pid}").read().strip()
                memory_info = os.popen(
                    f"nvidia-smi -i {gpu_id} --query-compute-apps=pid,used_memory --format=csv | grep {pid}").read().strip().split("\n")[0].split(", ")[1].split(" ")[0]
                result_list.append(
                    {"gpu_id": gpu_id, "pid": pid, "user": user, "memory_info": int(memory_info)})
    gpu_overall_info = {}
    for i in range(len(gpu_info)):
        gpu_overall_info[str(i)] = {
            "gpu_name": gpu_info[i].split(",")[0], "memory_total": gpu_info[i].split(",")[1], "memory_used": gpu_info[i].split(",")[2], "utilization": utilization_info[i]
        }
    return {"time": current_time, "gpu_overall_info": gpu_overall_info, "detail": result_list}


def get_every_gpu_usage(result):
    # 得到每张显卡的使用情况
    gpu_overall_info = result["gpu_overall_info"]
    gpu_num = len(gpu_overall_info)
    gpu_usage_result = {}
    for i in range(gpu_num):
        gpu_usage_result[str(i)] = {"gpu_name": gpu_overall_info[str(i)]["gpu_name"], "memory_total": gpu_overall_info[str(i)]["memory_total"], "memory_used": gpu_overall_info[str(i)]["memory_used"], "utilization": gpu_overall_info[str(i)]["utilization"], "user": {}}

    # 返回这个显卡中每个人使用的显存
    # user: {user1: memory_info1, user2: memory_info2}

    detail = result["detail"]
    for item in detail:
        gpu_id = item["gpu_id"]
        pid = item["pid"]
        memory_info = item["memory_info"]
        user = item["user"]
        
        # 实现一个卡上有多个人使用的情况
        if user not in gpu_usage_result[gpu_id]["user"].keys():
            gpu_usage_result[gpu_id]["user"][user] = memory_info
        else:
            gpu_usage_result[gpu_id]["user"][user] += memory_info
            
    return gpu_usage_result
        