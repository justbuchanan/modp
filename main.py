#!/usr/bin/env python3

import subprocess
import re


def window_ids():
    return subprocess.check_output(['lsw']).decode('utf-8').strip().split('\n')

def focused_window_id():
    return subprocess.check_output(['pfw']).decode('utf-8').strip()

def window_properties(id):
    xprop = subprocess.check_output(['xprop', '-id', str(id)]).decode('utf-8').strip()

    results = {}

    m = re.findall('_NET_WM_PID\(CARDINAL\) = (\d+)', xprop)[0]
    if m: results['pid'] = m

    m = re.findall('_NET_WM_DESKTOP\(CARDINAL\) = (\d+)', xprop)
    if m: results['desktop'] = m[0]

    m = re.findall('WM_NAME\(STRING\) = "([^\n"]+)', xprop)
    if m: results['name'] = m[0]

    m = re.findall('WM_NAME\(UTF8_STRING\) = "([^\n"]+)', xprop)
    if m: results['name'] = m[0]

    m = re.findall('WM_ICON_NAME\(STRING\) = "([^\n"]+)', xprop)
    if m: results['icon_name'] = m[0]

    m = re.findall('WM_WINDOW_ROLE\(STRING\) = "([^\n"]+)', xprop)
    if m: results['window_role'] = m[0]

    return results



if __name__ == '__main__':
    for win_id in window_ids():
        props = window_properties(win_id)
        print("Window: %s  " % win_id)
        # print("\n  %s: %s" % (prop))
        for key, value in props.items():
            print("  %s: %s" % (key, value))
        print()
