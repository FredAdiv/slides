# Multiprocess
{id: multiprocess}

## Multiprocess CPU count
{id: multiprocess-cpu-count}
{i: cpu_count}

* [multiprocessing](https://docs.python.org/library/multiprocessing.html)

![](examples/multiprocess/cpu_count.py)

## Multiprocess Process
{id: multiprocess-process}
{i: Process}

![](examples/multiprocess/cpu_count.py)


## Multiprocess N files: Pool
{id: multiprocess-file}
{i: multiprocess}
{i: Pool}
{i: map}

Analyze N files in parallel.

![](examples/multiprocess/multiprocess_files.py)

```
$ python multiprocess_files.py 3 multiprocess_*

Process 22688 analyzing multiprocess_files.py
Process 22689 analyzing multiprocess_load.py
Process 22690 analyzing multiprocess_pool_async.py
Process 22688 analyzing multiprocess_pool.py
{'filename': 'multiprocess_files.py', 'total': 833, 'digits': 10, 'spaces': 275}
{'filename': 'multiprocess_load.py', 'total': 694, 'digits': 14, 'spaces': 163}
{'filename': 'multiprocess_pool_async.py', 'total': 695, 'digits': 8, 'spaces': 161}
{'filename': 'multiprocess_pool.py', 'total': 397, 'digits': 3, 'spaces': 80}
```

{aside}
We asked it to use 3 processes, so looking at the process ID you can see one of them worked twice.
The returned results can be any Python datastructure. A dictionary is usually a good idea.
{/aside}


## Multiprocess load
{id: multiprocess-load}
{i: multiprocess}
{i: Pool}
{i: map}

![](examples/multiprocess/multiprocess_load.py)


## Multiprocess: Pool
{id: multiprocess-pool}
{i: multiprocess}
{i: Pool}
{i: map}

`Pool(3)` creates 3 child-processes and let's them compute the values. `map`
returns the results in the same order as the input came in.

![](examples/multiprocess/multiprocess_pool.py)

```
python multiprocess_pool.py  11 3
python multiprocess_pool.py  100 5
```


## Multiprocess load async
{id: multiprocess-load-async}
{i: imap}
{i: map_async}

![](examples/multiprocess/multiprocess_pool_async.py)


## Multiprocess and logging
{id: multiprocess-and-loggin}
{i: multiprocess}
{i: logging}

Tested on Windows

![](examples/multiprocess/multiprocessing_and_logging.py)

## Exercise: Process N files in parallel
{id: exercise-process-n-files-in-parallel}

Create N=100 files 1.txt - N.txt
In each file put L random strings of up to X characters

Write a script that will read all the files for each file and count how many times each digit appears. Then provide a combined report. First write the script in a single process way.
Then convert it to be able to work with multiprocess.

## Exercise: Process N Excel files in parallel
{id: exercise-process-n-excel-files-in-parallel}

* Create N Excel files with 10 random numbers in the first row of each file. This should be **create_random_excel.py**.
* Write a process that reads the N Excel files and sums up the numbers in each one of them and then sums up the numbers of all the files. This should be **add_excel.py** that gets the list of Excel files on the command line.

## Exercise: Fetch URLs in parallel
{id: exercise-fetch-urls-in-parallel}

* [top-websites](https://www.similarweb.com/top-websites)
* Given a file with a list of URLs, collect the title of each site.

![](examples/parallel/urls.txt)

![](examples/parallel/fetch_urls.py)

## Exercise: Fetch URLs from one site.
{id: exercise-fetch-urls-from-one-site}

Download the [sitemap](https://code-maven.com/sitemap.xml) or the other [sitemap](the https://code-maven.com/slides/sitemap.xml) file
and fetch the first N URLs from there. Collecting the titles.

![](examples/parallel/fetch_site_urls.py)

## Solution: Fetch URLs in parallel
{id: solution-fetch-urls-in-parallel}

* First create function and use regular map.
* Deal with encoding.
* Replace continue by return, include None in results.
* It has some 2 sec overhead, but then 20 items reduced from 18 sec to 7 sec using pool of 5.

![](examples/parallel/fetch_urls_multiprocess.py)

