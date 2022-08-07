from db_connection import get_db_connection

def drop_tables(con):
    cur = con.cursor()

    cur.execute('drop table if exists sensors;')
    cur.execute('drop table if exists notes;')
    cur.execute('drop table if exists sensor_readings;')

    con.commit()

def create_sensors_table(con):
    cur = con.cursor()
    cur.execute('''
        create table sensors (
            mac text primary key,
            name text
        );
    ''')
    con.commit()

def create_notes_table(con):
    cur = con.cursor()
    cur.execute('''
        create table notes (
            id integer primary key autoincrement,
            note text,
            datetime text,
            sensor text,
            foreign key(sensor) references sensors(mac)
        );
    ''')
    con.commit()

def create_sensor_readings_table(con):
    cur = con.cursor()
    cur.execute('''
        create table sensor_readings (
            id integer primary key autoincrement,
            data_format integer,
            humidity real,
            temperature real,
            pressure real,
            acceleration real,
            acceleration_x integer,
            acceleration_y integer,
            acceleration_z integer,
            tx_power integer,
            battery real,
            movement_counter integer,
            measurement_sequence_number integer,
            sensor text,
            foreign key(sensor) references sensors(mac)
        );
    ''')
    con.commit()

#{
#    'data_format': 5, 
#    'humidity': 42.75, 
#    'temperature': 24.54, 
#    'pressure': 1015.43, 
#    'acceleration': 1040.6536407470066, 
#    'acceleration_x': 8, 
#    'acceleration_y': -36, 
#    'acceleration_z': 1040, 
#    'tx_power': 4, 
#    'battery': 2992, 
#    'movement_counter': 45, 
#    'measurement_sequence_number': 5646, 
#    'mac': 'd92e2aee6843'
#}

def main():
    connection = get_db_connection()

    drop_tables(connection)
    create_sensors_table(connection)
    create_notes_table(connection)
    create_sensor_readings_table(connection)


if __name__ == "__main__":
    main()