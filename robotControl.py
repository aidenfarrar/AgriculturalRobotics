import socket
import time

HOST = "169.254.14.134"  # Laptop (server) IP address.
PORT = 30002

print("Starting Python program:")
count = 0

while (count < 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))  # Bind to the port.
    s.listen(5)  # Wait for UR3 (client) connection.
    c, addr = s.accept()  # Establish connection with client.

    try:
        msg = c.recv(1024).decode()  # Receive message from UR3.
        if msg == 'UR3_is_asking_for_data':
            print("   UR3 is asking for data...")
            count = count + 1
            print("   count = ", count)
            time.sleep(0.5)

            # Cartesian tool pose (X,Y,Z,Roll,Pitch,Yaw).  Note: units are meter and rad.
            # pose = [-0.113, -0.163, 0.451, -1.5708, 0, 0]  # e.g., home
            pose = [0.358, -0.102, 0.278, -1.458, -0.020, 0.372]  # e.g., viewPose1

            values = str(pose[0]) + "," + str(pose[1]) + "," + str(pose[2]) + "," + str(pose[3]) + "," + str(
                pose[4]) + "," + str(pose[5])
            poseString = "(" + values + ")"
            print("   Pose string data to send: " + poseString)
            c.send(poseString.encode());

    except socket.error as socketerror:
        print(count)

c.close()
s.close()
print("Ending program.")