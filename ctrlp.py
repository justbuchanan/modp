#!/usr/bin/env python3

from subprocess import check_output


wminfo = []
desktop_list = []

monitor_names = check_output(['bspc', 'query', '-M']).decode('utf-8').strip().split('\n')
for monitor in monitor_names:
    print('%s' % monitor)
    desktop_names = check_output(['bspc', 'query', '-D', '-m', monitor]).decode('utf-8').strip().split('\n')
    # print(desktop_names)

    # print('  ' + "\n  ".join(desktop_names))

    out = "  "

    for dname in desktop_names:
        desktop_list.append(dname)
        out += "%d: %s" % (len(desktop_list)-1, dname)
        out += '\n  '
    print(out)


    # desktop_list.append(desktop_names)



num = int(input("desktop: "))


dname = desktop_list[num]



check_output(['bspc', 'desktop', dname, '--focus', ])


