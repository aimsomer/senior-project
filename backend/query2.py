import sqlite3
import pandas
import csv


def create_table():
    try:
        with sqlite3.connect("db2.sqlite") as con:
            # con.execute('DROP TABLE IF EXIST t1')
            cmd = """
            create table ap1_1(

                BSSID text,
                First_time_seen text,
                Last_time_seen text,
                channel integer,
                Speed integer,
                Privacy text,
                Cipher text,
                Authentication text,
                Power integer,
                beacons integer,
                IV integer,
                LAN_IP text, 
                ID_length integer,
                ESSID text,
                Key text
            );
            """
            con.execute(cmd)

            cmd2 = """
            create table sta1_1(
                Station_MAC text,
                First_time_seen text,
                Last_time_seen text,
                Power integer,
                packets integer,
                BSSID text,
                Probed_ESSIDs text
            );
            """
            con.execute(cmd2)

    except Exception as e:
        print(f"Error -> {e}")

def insert():
    fname = input("csv file name: ")
    try:
        with sqlite3.connect("db2.sqlite") as con:
            cur = con.cursor()
            with open(fname, 'r') as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    # print(row)
                    if i == 0 or i == 32:
                        continue
                    if i <= 31:
                        BSSID = row[0]
                        First_time_seen = row[1]
                        Last_time_seen  = row[2]
                        channel = row[3]
                        Speed = row[4]
                        Privacy = row[5]
                        Cipher = row[6]
                        Authentication = row[7]
                        Power = row[8]
                        beacons = row[9]
                        IV = row[10]
                        LAN_IP  = row[11]
                        ID_length= row[12]
                        ESSID = row[13]
                        Key = row[14]
                        con.execute(
                        ''' 
                        INSERT INTO ap1_1(BSSID, First_time_seen, Last_time_seen, channel, speed, 
                        Privacy, Cipher, Authentication, power, beacons, IV, LAN_IP, ID_length, ESSID, Key)
                        VALUES (?,?,?,?,?,
                                ?,?,?,?,?,
                                ?,?,?,?,?)
                        ''',(BSSID, First_time_seen, Last_time_seen, channel, Speed, 
                        Privacy, Cipher, Authentication, Power, beacons, IV, LAN_IP, ID_length, ESSID, Key)
                        )
                    elif i > 33:
                        Station_MAC = row[0]
                        First_time_seen2 = row[1]
                        Last_time_seen2 = row[2]
                        Power2 = row[3]
                        packets = row[4]
                        BSSID2 = row[5]
                        Probed_ESSIDs = row[6]
                        con.execute(
                        '''
                        INSERT INTO sta1_1(Station_MAC, First_time_seen, 
                        Last_time_seen, Power, packets, BSSID, Probed_ESSIDs)
                        VALUES(?,?,?,?,?,?,?)
                        ''',
                        (Station_MAC, First_time_seen2, Last_time_seen2, Power2, packets, BSSID2, Probed_ESSIDs)
                        )
                    
                    con.commit()

    except Exception as e:
        print(f"Error -> {e}")

if __name__ == "__main__":
    create_table()
    insert()
