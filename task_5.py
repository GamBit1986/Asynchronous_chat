import subprocess

args_ya = ["ping", "-c 3", "yandex.ru"]
args_you = ["ping", "-c 3", "youtube.com"]

ping_result_ya = subprocess.Popen(args_ya, stdout=subprocess.PIPE)
ping_result_you = subprocess.Popen(args_you, stdout=subprocess.PIPE)

for line in ping_result_ya.stdout:
    print(line.decode("UTF-8"))

for line in ping_result_you.stdout:
    print(line.decode("UTF-8"))
