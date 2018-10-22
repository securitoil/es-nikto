import csv
import subprocess

def handle(options):
    """
    Run nikto against the specified host and port
    Args:
        options (dict): json request body
    """
    result = subprocess.check_output(['nikto', '-host', options['host'], '-port', options['port'],
                                      '-Format', 'csv', '-output', '-'])
    results = []
    csvreader = csv.reader(result, delimiter=',', quotechar='"')
    for row in csvreader:
        if len(row) > 1:
            results.append({
                'host': row[0],
                'port': int(row[2]),
                'osbdb': row[3],
                'method': row[4],
                'path': row[5],
                'comment': row[6]
            })
    return results
