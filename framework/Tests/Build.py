import os
import paramiko


def get_build(url,location):
    """
    :param url: Build url (Taking from Latest)
    :param location: Download location on local machine
    """
    try:
        os.system('wget --no-parent -R index.* -r ' + url + ' -P ' + location)
    except Exception as e:
        print(str(e))



def upload_GVM(location, userName, pemFile, publicDNS):
    """
    :param location: Path of Build Download location (local machine)
    :param userName: User name of Guest machine
    :param pemFile: .pem file location
    :param publicDNS: Guest machine Public DNS ID
    """
    try:
        path_LinuxUVM = location + "172.22.15.73/builds/latest/Linux_UVM/"

        command = 'scp -i ' + pemFile + ' -r '+ path_LinuxUVM + ' ' + userName + '@'+ publicDNS + ':~'
        os.system(command=command)
        print(command)
    except Exception as e:
        print(str(e))



def upload_CVM(location, userName, pemFile, publicDNS):
    pass


def connect_instance(pemFile, publicDNS, userName):
    """
    :param pemFile: AWS pem file location
    :param publicDNS: public DNS of Instance
    :param userName: Instance User name
    :return: ssh session object
    """
    sshKey = paramiko.RSAKey.from_private_key_file(pemFile)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(publicDNS, username=userName, pkey=sshKey)
    return ssh


url = 'http://172.22.15.73/builds/latest/'
location = '~/Build/'
pemFile = '/home/aaftabizt/NUTANIX_Xtract/AWS_keys/Aaftab_London_Key.pem'

publicDNS_GVM = 'ec2-18-130-220-214.eu-west-2.compute.amazonaws.com'
userName_GVM = 'ec2-user'


publicDNS_CVM = 'ec2-18-130-220-239.eu-west-2.compute.amazonaws.com'
userName_CVM = 'centos'


# get_build(url, location)                                   # Download Build from Jenkins


ssh_GVM = connect_instance(pemFile, publicDNS_GVM, userName_GVM)

# upload_GVM(location, userName_GVM, pemFile, publicDNS_GVM)      # upload Linux_UVM on GVM


stdin, stdout, stderr = ssh_GVM.exec_command("sudo rm -rf Linux_UVM/")
print(stdout.read().decode('utf-8'))

stdin, stdout, stderr = ssh_GVM.exec_command("sudo rm -rf /usr/sbin/cbtctl /usr/sbin/nxcbt.ko /usr/sbin/snapshotOps.py /usr/sbin/snapshotOps_main.py")
print(stdout.read().decode('utf-8'))


stdin, stdout, stderr = ssh_GVM.exec_command("sudo cp Linux_UVM/* /usr/sbin/")
print(stdout.read().decode('utf-8'))


stdin, stdout, stderr = ssh_GVM.exec_command("ls -ltr /usr/sbin/ | grep cbt")
print(stdout.read().decode('utf-8'))



