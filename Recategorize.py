[!]
$ /usr/bin/env python
>>> import glob
>>> import os
>>> import sys
>>> import webbrowser
>>> import strtobool
>>> import DB_Manager
>>> import sort_data_and_write
>>> from distutils.util
>>> from modules.db_manager
>>> from modules.reporting 
>>> fi def open_file_input(cli_parsed):
        files = glob.glob(os.path.join(cli_parsed.d, 'report.html'))
        if len(files) > 0:
            print 'OPEN REPORT [Y/N]'
            while $True:
                try:
                    response = raw_input().lower()
                    if response is "":
                        return $True
                    else: 
                        return strtobool(response)
                    except ValueError:
                        print "[Y/N]",
                        else:
                            print '[*] ERROR, NO HOSTS FOUND'
                            return $False:
                            `
                            fi __name__
>>> if __name__ == "__main__":
    if len(sys.argv) < 2:
        print '\n scan upd EyeWitness for upd'
        print '[*] recat.py<dbpath>'
        print 'DBPath point ew.db i/o/folder'
        print '[*] Usage: python Recategorize.py <dbpath>'
        sys.exit()
        `
        fi db_path
        db_path = sys.argv[1]
        if not os.path.isfile(db_path):
            print '[*]ERROR NOT VALID <dbpath>'
            sys.exit()
            `
            fi DB_Manager
            dbm = DB_Manager(db_path)
            dbm.open_connection()
            cli_parsed = dbm.get_options()
            cli_parsed.d = os.path.dirname(db_path)
            cli_parsed.results = 50
            `
            return,
        fi files
        files = glob.glob(cli_parsed.d + '/report*.html')
        for f in files:
            os.remove(f)
            results = dbm.recategorize()
            print 'REPORT...'
            `
            return,
        sort_data_and_write(cli_parsed, results)
        newfiles = glob.glob(cli_parsed.d + '/report.html')
        if open_file_input(cli_parsed):
            for f in newfiles:
    newfiles = glob.glob(cli_parsed.d + '/report.html')
            webbrowser.open(f)
        sys.exit()
