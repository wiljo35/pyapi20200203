#!/usr/bin/python3

import numpy as np # number operations
import yaml # pyyaml for yaml
import re  # regex
import paramiko # ssh into servers
from flask import Flask, render_template
import matplotlib.pyplot as plt

def sshlogin(ip, un, passw):
    sshsession = paramiko.SSHClient()
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshsession.connect(hostname=ip, username=un, password=passw)
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command("cat /proc/uptime")
    sshresult = ssh_stdout.read().decode('utf-8').split()[1]
    with open("sshresult", "w") as myfile:
        myfile.write(sshresult)
    mins = (int(float(sshresult)) / 60)  # convert uptime in sec to mins
    sshsession.close()
    return mins

app = Flask(__name__)

@app.route("/graphin")
def graphin():
    with open("/home/student/sshpass.yml") as sshpass: # creds for our servers
        creds = yaml.load(sshpass)
    svruptime = []
    xtick = []
    for cred in creds:
        xtick.append(cred['ip'])
        resp = sshlogin(cred['ip'], cred['un'], cred['passw'])
        svruptime.append(resp)
    xtick = tuple(xtick) # create a tuple
    svruptime = tuple(svruptime)

    # graphin
    N = 2 # total number of bars
    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence
    p1 = plt.bar(ind, svruptime, width)  ## <--- ! Erroring here

    plt.ylabel('Uptime in Minutes')

    plt.title('Uptime of Servers in Minutes')
    plt.xticks(ind, xtick)
    plt.yticks(np.arange(0, 200, 10)) # prob want to turn this into a log scale
    # plt.legend((p1[0],), ('Servers',))

    plt.savefig('static/status.png') # might want to save this with timestamp for history purposes
    return render_template("graph.html")

if __name__ == "__main__":
    app.run(port=5006)
