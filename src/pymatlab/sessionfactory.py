# -*- coding: iso-8859-15 -*-
'''
Copyright 2010-2013 Joakim Möller

This file is part of pymatlab.

pymatlab is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pymatlab is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pymatlab.  If not, see <http://www.gnu.org/licenses/>.
'''

import os
import os.path
import platform

from pymatlab.matlab import MatlabSession

def session_factory(options='',output_buffer_size=8096):
    system = platform.system()
    path = None
    if (system == 'Linux') or (system == 'Darwin'):
        # find the MATLAB-root path:
        locations = os.environ.get("PATH").split(os.pathsep)
        for location in locations:
            candidate = os.path.join(location, 'matlab')
            if os.path.isfile(candidate):
                path = candidate
                break
        executable = os.path.realpath(path)
        basedir = os.path.dirname(os.path.dirname(executable))
        exec_and_options = " ".join([executable,options])
        session = MatlabSession(basedir,exec_and_options,output_buffer_size)
    elif system =='Windows':
        locations = os.environ.get("PATH").split(os.pathsep)
        for location in locations:
            candidate = os.path.join(location, 'matlab.exe')
            if os.path.isfile(candidate):
                path = candidate
                break
        executable = os.path.realpath(path)
        basedir = os.path.dirname(os.path.dirname(executable))
        session = MatlabSession(path=basedir,bufsize=output_buffer_size)

    else:
        raise NotSupportedException(
                'Not supported on the {platform}-platform'.format(
                        platform=system))
    return session

def remote_session_factory(hostname,remote_path):
    system = platform.system()
    path = None
    if (system == 'Linux') or (system == 'Darwin'):
        locations = os.environ.get("PATH").split(os.pathsep)
        for location in locations:
            candidate = os.path.join(location, 'matlab')
            if os.path.isfile(candidate):
                path = candidate
                break
        executable = os.path.realpath(path)
        basedir = os.path.dirname(os.path.dirname(executable))
        session = MatlabSession(
            basedir,
            "ssh {host} '/bin/csh -c {full_path}'".format(
                    host=hostname,
                    full_path=remote_path)
            )
    else:
        raise NotSupportedException(
                'Not supported on the {platform}-platform'.format(
                        platform=system))
    return session

