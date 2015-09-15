##1. Error: RuntimeError: Running cythonize failed!
###1.1 Message:
    Running from numpy source directory.
    
    Cythonizing sources

    Processing numpy/random/mtrand/mtrand.pyx

    Traceback (most recent call last):

        File "<string>", line 1, in <module>

        ImportError: No module named Cython.Compiler.Main

        Traceback (most recent call last):

        File "/c4_working/rest_work/github/numpy/numpy/tools/cythonize.py", line 199, in <module>

        main()

        File "/c4_working/rest_work/github/numpy/numpy/tools/cythonize.py", line 195, in main

        find_process_files(root_dir)

        File "/c4_working/rest_work/github/numpy/numpy/tools/cythonize.py", line 187, in find_process_files

        process(cur_dir, fromfile, tofile, function, hash_db)

        File "/c4_working/rest_work/github/numpy/numpy/tools/cythonize.py", line 161, in process

        processor_function(fromfile, tofile)

        File "/c4_working/rest_work/github/numpy/numpy/tools/cythonize.py", line 81, in process_pyx

        raise Exception('Cython failed')

        Exception: Cython failed

                   Traceback (most recent call last):

        File "setup.py", line 260, in <module>

        setup_package()

        File "setup.py", line 248, in setup_package

        generate_cython()

        File "setup.py", line 199, in generate_cython

        raise RuntimeError("Running cythonize failed!")

        RuntimeError: Running cythonize failed!

###1.2 Command: 
python setup.py build --fcompiler=gnu

###1.3 Reason:  
Numpy has some code written by Cython language (like numpy/random/mtrand/mtrand.pyx), the expected compiler of Cython was missed. you have to install Cython to fix this issue.
