import sys
import paramiko

class RemoteJtopMeasure:
    def __init__(self, hostname, username, password, script_dir):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.script_dir = script_dir
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def start(self):
        try:
            self.ssh_client.connect(self.hostname, username=self.username, password=self.password)
            print("###################Début de la mesure jtop###########################")

            # Command to execute the start script
            command = f"sudo {self.script_dir}/script_start_tx.sh > /dev/null 2>&1 &"
            stdin, stdout, stderr = self.ssh_client.exec_command(command)
            print(stdout.read().decode())
            print(stderr.read().decode())  # Print errors if any
        except Exception as e:
            print(f"Erreur lors de la connexion SSH ou de l'exécution du script : {e}")

    def stop(self):
        try:
            if not self.ssh_client.get_transport() or not self.ssh_client.get_transport().is_active():
                print("SSH connection is not active. Reconnecting...")
                self.ssh_client.connect(self.hostname, username=self.username, password=self.password)

            # Command to execute the stop script
            command = f"sudo {self.script_dir}/script_stop_tx.sh"
            stdin, stdout, stderr = self.ssh_client.exec_command(command)
            print(stdout.read().decode())
            print(stderr.read().decode())  # Print errors if any
            print("###################Fin de la mesure jtop###########################")
        except Exception as e:
            print(f"Erreur lors de l'arrêt du script : {e}")
        finally:
            if self.ssh_client.get_transport() and self.ssh_client.get_transport().is_active():
                self.ssh_client.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        action = sys.argv[1]
        remote_measure = RemoteJtopMeasure(
            hostname="10.42.0.64",
            username="sshuser",
            password="nvidia",
            script_dir="/media/nvidia/00640565-37a8-4b58-a27b-fbd90cd43fec/inference_results_v4.1/closed/NVIDIA/code"
        )

        if action == "start":
            remote_measure.start()
        elif action == "stop":
            remote_measure.stop()
        else:
            print("Invalid action. Use 'start' or 'stop'.")
    else:
        print("Usage: python remote_jtop_measure.py [start|stop]")
