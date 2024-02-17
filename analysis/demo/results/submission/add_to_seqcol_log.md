### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo1_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-15 19:23:28) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e3220166a77e53e0c1fbb4757fd0c8651e7bc9fc
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-15 09:28:29 -0500
*        Pipeline diff:  5 files changed, 52 insertions(+), 15 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo1


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo1
pipestat record identifier: demo1
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target to produce: `data/demo/demo1.fa.checksums`  

> `checksumseq --input data/demo/demo1.fa --output data/demo/demo1.fa.checksums` (50931)
<pre>
thread 'main' panicked at /home/nsheff/.cargo/registry/src/index.crates.io-6f17d22bba15001f/rust-gc-count-0.1.0/src/checksumseq.rs:47:41:
called `Result::unwrap()` on an `Err` value: Os { code: 2, kind: NotFound, message: "No such file or directory" }
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
</pre>
Command completed. Elapsed time: 0:00:00. Running peak memory: 0GB.  
  PID: 50931;	Command: checksumseq;	Return code: 101;	Memory used: 0.0GB


### Pipeline failed at:  (02-15 19:23:28) elapsed: 0.0 _TIME_

Total time: 0:00:00
Failure reason: Subprocess returned nonzero result. Check above output for details
Traceback (most recent call last):
  File "/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py", line 63, in <module>
    pm.run(command, target)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 1083, in run
    process_return_code, local_maxmem = self.callprint(
                                        ^^^^^^^^^^^^^^^
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 1352, in callprint
    self._triage_error(SubprocessError(msg), nofail)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2575, in _triage_error
    self.fail_pipeline(e)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2045, in fail_pipeline
    raise exc
pypiper.exceptions.SubprocessError: Subprocess returned nonzero result. Check above output for details
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo2_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-15 19:23:29) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e3220166a77e53e0c1fbb4757fd0c8651e7bc9fc
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-15 09:28:29 -0500
*        Pipeline diff:  5 files changed, 52 insertions(+), 15 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo2


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo2
pipestat record identifier: demo2
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target to produce: `data/demo/demo2.fa.checksums`  

> `checksumseq --input data/demo/demo2.fa --output data/demo/demo2.fa.checksums` (50966)
<pre>
thread 'main' panicked at /home/nsheff/.cargo/registry/src/index.crates.io-6f17d22bba15001f/rust-gc-count-0.1.0/src/checksumseq.rs:47:41:
called `Result::unwrap()` on an `Err` value: Os { code: 2, kind: NotFound, message: "No such file or directory" }
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
</pre>
Command completed. Elapsed time: 0:00:00. Running peak memory: 0GB.  
  PID: 50966;	Command: checksumseq;	Return code: 101;	Memory used: 0.0GB


### Pipeline failed at:  (02-15 19:23:29) elapsed: 0.0 _TIME_

Total time: 0:00:00
Failure reason: Subprocess returned nonzero result. Check above output for details
Traceback (most recent call last):
  File "/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py", line 63, in <module>
    pm.run(command, target)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 1083, in run
    process_return_code, local_maxmem = self.callprint(
                                        ^^^^^^^^^^^^^^^
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 1352, in callprint
    self._triage_error(SubprocessError(msg), nofail)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2575, in _triage_error
    self.fail_pipeline(e)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2045, in fail_pipeline
    raise exc
pypiper.exceptions.SubprocessError: Subprocess returned nonzero result. Check above output for details
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo3_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-15 19:23:30) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e3220166a77e53e0c1fbb4757fd0c8651e7bc9fc
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-15 09:28:29 -0500
*        Pipeline diff:  5 files changed, 52 insertions(+), 15 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo3


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo3
pipestat record identifier: demo3
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target to produce: `data/demo/demo3.fa.checksums`  

> `checksumseq --input data/demo/demo3.fa --output data/demo/demo3.fa.checksums` (51004)
<pre>
thread 'main' panicked at /home/nsheff/.cargo/registry/src/index.crates.io-6f17d22bba15001f/rust-gc-count-0.1.0/src/checksumseq.rs:47:41:
called `Result::unwrap()` on an `Err` value: Os { code: 2, kind: NotFound, message: "No such file or directory" }
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
</pre>
Command completed. Elapsed time: 0:00:00. Running peak memory: 0GB.  
  PID: 51004;	Command: checksumseq;	Return code: 101;	Memory used: 0.0GB


### Pipeline failed at:  (02-15 19:23:30) elapsed: 0.0 _TIME_

Total time: 0:00:00
Failure reason: Subprocess returned nonzero result. Check above output for details
Traceback (most recent call last):
  File "/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py", line 63, in <module>
    pm.run(command, target)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 1083, in run
    process_return_code, local_maxmem = self.callprint(
                                        ^^^^^^^^^^^^^^^
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 1352, in callprint
    self._triage_error(SubprocessError(msg), nofail)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2575, in _triage_error
    self.fail_pipeline(e)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2045, in fail_pipeline
    raise exc
pypiper.exceptions.SubprocessError: Subprocess returned nonzero result. Check above output for details
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo4_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-15 19:23:31) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e3220166a77e53e0c1fbb4757fd0c8651e7bc9fc
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-15 09:28:29 -0500
*        Pipeline diff:  5 files changed, 52 insertions(+), 15 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo4


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo4
pipestat record identifier: demo4
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target to produce: `data/demo/demo4.fa.checksums`  

> `checksumseq --input data/demo/demo4.fa --output data/demo/demo4.fa.checksums` (51040)
<pre>
thread 'main' panicked at /home/nsheff/.cargo/registry/src/index.crates.io-6f17d22bba15001f/rust-gc-count-0.1.0/src/checksumseq.rs:47:41:
called `Result::unwrap()` on an `Err` value: Os { code: 2, kind: NotFound, message: "No such file or directory" }
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
</pre>
Command completed. Elapsed time: 0:00:00. Running peak memory: 0GB.  
  PID: 51040;	Command: checksumseq;	Return code: 101;	Memory used: 0.0GB


### Pipeline failed at:  (02-15 19:23:31) elapsed: 0.0 _TIME_

Total time: 0:00:00
Failure reason: Subprocess returned nonzero result. Check above output for details
Traceback (most recent call last):
  File "/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py", line 63, in <module>
    pm.run(command, target)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 1083, in run
    process_return_code, local_maxmem = self.callprint(
                                        ^^^^^^^^^^^^^^^
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 1352, in callprint
    self._triage_error(SubprocessError(msg), nofail)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2575, in _triage_error
    self.fail_pipeline(e)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2045, in fail_pipeline
    raise exc
pypiper.exceptions.SubprocessError: Subprocess returned nonzero result. Check above output for details
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo5_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-15 19:23:32) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e3220166a77e53e0c1fbb4757fd0c8651e7bc9fc
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-15 09:28:29 -0500
*        Pipeline diff:  5 files changed, 52 insertions(+), 15 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo5


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo5
pipestat record identifier: demo5
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target to produce: `data/demo/demo5.fa.checksums`  

> `checksumseq --input data/demo/demo5.fa --output data/demo/demo5.fa.checksums` (51076)
<pre>
thread 'main' panicked at /home/nsheff/.cargo/registry/src/index.crates.io-6f17d22bba15001f/rust-gc-count-0.1.0/src/checksumseq.rs:47:41:
called `Result::unwrap()` on an `Err` value: Os { code: 2, kind: NotFound, message: "No such file or directory" }
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
</pre>
Command completed. Elapsed time: 0:00:00. Running peak memory: 0GB.  
  PID: 51076;	Command: checksumseq;	Return code: 101;	Memory used: 0.0GB


### Pipeline failed at:  (02-15 19:23:32) elapsed: 0.0 _TIME_

Total time: 0:00:00
Failure reason: Subprocess returned nonzero result. Check above output for details
Traceback (most recent call last):
  File "/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py", line 63, in <module>
    pm.run(command, target)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 1083, in run
    process_return_code, local_maxmem = self.callprint(
                                        ^^^^^^^^^^^^^^^
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 1352, in callprint
    self._triage_error(SubprocessError(msg), nofail)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2575, in _triage_error
    self.fail_pipeline(e)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2045, in fail_pipeline
    raise exc
pypiper.exceptions.SubprocessError: Subprocess returned nonzero result. Check above output for details
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo6_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-15 19:27:32) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e3220166a77e53e0c1fbb4757fd0c8651e7bc9fc
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-15 09:28:29 -0500
*        Pipeline diff:  5 files changed, 52 insertions(+), 15 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo6


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo6
pipestat record identifier: demo6
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target to produce: `/home/nsheff/code/seqcolapi/data/demo/demo6.fasta.checksums`  

> `checksumseq --input /home/nsheff/code/seqcolapi/data/demo/demo6.fasta --output /home/nsheff/code/seqcolapi/data/demo/demo6.fasta.checksums` (51391)
<pre>
thread 'main' panicked at /home/nsheff/.cargo/registry/src/index.crates.io-6f17d22bba15001f/rust-gc-count-0.1.0/src/checksumseq.rs:47:41:
called `Result::unwrap()` on an `Err` value: Os { code: 2, kind: NotFound, message: "No such file or directory" }
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
</pre>
Command completed. Elapsed time: 0:00:00. Running peak memory: 0GB.  
  PID: 51391;	Command: checksumseq;	Return code: 101;	Memory used: 0.0GB


### Pipeline failed at:  (02-15 19:27:32) elapsed: 0.0 _TIME_

Total time: 0:00:00
Failure reason: Subprocess returned nonzero result. Check above output for details
Traceback (most recent call last):
  File "/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py", line 63, in <module>
    pm.run(command, target)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 1083, in run
    process_return_code, local_maxmem = self.callprint(
                                        ^^^^^^^^^^^^^^^
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 1352, in callprint
    self._triage_error(SubprocessError(msg), nofail)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2575, in _triage_error
    self.fail_pipeline(e)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2045, in fail_pipeline
    raise exc
pypiper.exceptions.SubprocessError: Subprocess returned nonzero result. Check above output for details
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo0_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-15 19:29:27) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e3220166a77e53e0c1fbb4757fd0c8651e7bc9fc
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-15 09:28:29 -0500
*        Pipeline diff:  5 files changed, 52 insertions(+), 15 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo0


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo0
pipestat record identifier: demo0
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target to produce: `/home/nsheff/code/seqcolapi/data/demo/demo0.fa.checksums`  

> `checksumseq --input /home/nsheff/code/seqcolapi/data/demo/demo0.fa --output /home/nsheff/code/seqcolapi/data/demo/demo0.fa.checksums` (51595)
<pre>
thread 'main' panicked at /home/nsheff/.cargo/registry/src/index.crates.io-6f17d22bba15001f/rust-gc-count-0.1.0/src/checksumseq.rs:47:41:
called `Result::unwrap()` on an `Err` value: Os { code: 2, kind: NotFound, message: "No such file or directory" }
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
</pre>
Command completed. Elapsed time: 0:00:00. Running peak memory: 0GB.  
  PID: 51595;	Command: checksumseq;	Return code: 101;	Memory used: 0.0GB


### Pipeline failed at:  (02-15 19:29:27) elapsed: 0.0 _TIME_

Total time: 0:00:00
Failure reason: Subprocess returned nonzero result. Check above output for details
Traceback (most recent call last):
  File "/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py", line 63, in <module>
    pm.run(command, target)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 1083, in run
    process_return_code, local_maxmem = self.callprint(
                                        ^^^^^^^^^^^^^^^
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 1352, in callprint
    self._triage_error(SubprocessError(msg), nofail)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2575, in _triage_error
    self.fail_pipeline(e)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2045, in fail_pipeline
    raise exc
pypiper.exceptions.SubprocessError: Subprocess returned nonzero result. Check above output for details
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo1_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-15 19:29:28) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e3220166a77e53e0c1fbb4757fd0c8651e7bc9fc
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-15 09:28:29 -0500
*        Pipeline diff:  5 files changed, 52 insertions(+), 15 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo1


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo1
pipestat record identifier: demo1
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target to produce: `/home/nsheff/code/seqcolapi/data/demo/demo1.fa.checksums`  

> `checksumseq --input /home/nsheff/code/seqcolapi/data/demo/demo1.fa --output /home/nsheff/code/seqcolapi/data/demo/demo1.fa.checksums` (51630)
<pre>
thread 'main' panicked at /home/nsheff/.cargo/registry/src/index.crates.io-6f17d22bba15001f/rust-gc-count-0.1.0/src/checksumseq.rs:47:41:
called `Result::unwrap()` on an `Err` value: Os { code: 2, kind: NotFound, message: "No such file or directory" }
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
</pre>
Command completed. Elapsed time: 0:00:00. Running peak memory: 0GB.  
  PID: 51630;	Command: checksumseq;	Return code: 101;	Memory used: 0.0GB


### Pipeline failed at:  (02-15 19:29:28) elapsed: 0.0 _TIME_

Total time: 0:00:00
Failure reason: Subprocess returned nonzero result. Check above output for details
Traceback (most recent call last):
  File "/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py", line 63, in <module>
    pm.run(command, target)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 1083, in run
    process_return_code, local_maxmem = self.callprint(
                                        ^^^^^^^^^^^^^^^
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 1352, in callprint
    self._triage_error(SubprocessError(msg), nofail)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2575, in _triage_error
    self.fail_pipeline(e)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2045, in fail_pipeline
    raise exc
pypiper.exceptions.SubprocessError: Subprocess returned nonzero result. Check above output for details
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo0_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-15 19:30:51) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e3220166a77e53e0c1fbb4757fd0c8651e7bc9fc
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-15 09:28:29 -0500
*        Pipeline diff:  5 files changed, 52 insertions(+), 15 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo0


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo0
pipestat record identifier: demo0
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target exists: `/home/nsheff/code/seqcolapi/analysis/data/demo/demo0.fa.checksums`  
Traceback (most recent call last):
  File "/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py", line 77, in <module>
    from scconf import RDBDict
ModuleNotFoundError: No module named 'scconf'

### Pipeline failed at:  (02-15 19:30:51) elapsed: 0.0 _TIME_

Total time: 0:00:00
Failure reason: Pipeline failure. See details above.
Exception ignored in atexit callback: <bound method PipelineManager._exit_handler of <pypiper.manager.PipelineManager object at 0x7f05d57c4d90>>
Traceback (most recent call last):
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2201, in _exit_handler
    self.fail_pipeline(Exception("Pipeline failure. See details above."))
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2045, in fail_pipeline
    raise exc
Exception: Pipeline failure. See details above.
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo1_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-15 19:30:52) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e3220166a77e53e0c1fbb4757fd0c8651e7bc9fc
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-15 09:28:29 -0500
*        Pipeline diff:  5 files changed, 52 insertions(+), 15 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo1


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo1
pipestat record identifier: demo1
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target to produce: `/home/nsheff/code/seqcolapi/analysis/data/demo/demo1.fa.checksums`  

> `checksumseq --input /home/nsheff/code/seqcolapi/analysis/data/demo/demo1.fa --output /home/nsheff/code/seqcolapi/analysis/data/demo/demo1.fa.checksums` (51868)
<pre>
</pre>
Command completed. Elapsed time: 0:00:00. Running peak memory: 0GB.  
  PID: 51868;	Command: checksumseq;	Return code: 0;	Memory used: 0.0GB

Traceback (most recent call last):
  File "/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py", line 77, in <module>
    from scconf import RDBDict
ModuleNotFoundError: No module named 'scconf'

### Pipeline failed at:  (02-15 19:30:52) elapsed: 0.0 _TIME_

Total time: 0:00:00
Failure reason: Pipeline failure. See details above.
Exception ignored in atexit callback: <bound method PipelineManager._exit_handler of <pypiper.manager.PipelineManager object at 0x7f5bcc7c4610>>
Traceback (most recent call last):
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2201, in _exit_handler
    self.fail_pipeline(Exception("Pipeline failure. See details above."))
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2045, in fail_pipeline
    raise exc
Exception: Pipeline failure. See details above.
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo0_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-15 20:21:24) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e3220166a77e53e0c1fbb4757fd0c8651e7bc9fc
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-15 09:28:29 -0500
*        Pipeline diff:  5 files changed, 52 insertions(+), 15 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo0


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo0
pipestat record identifier: demo0
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target exists: `/home/nsheff/code/seqcolapi/analysis/data/demo/demo0.fa.checksums`  
Traceback (most recent call last):
  File "/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py", line 77, in <module>
    from scconf import RDBDict
ModuleNotFoundError: No module named 'scconf'

### Pipeline failed at:  (02-15 20:21:24) elapsed: 0.0 _TIME_

Total time: 0:00:00
Failure reason: Pipeline failure. See details above.
Exception ignored in atexit callback: <bound method PipelineManager._exit_handler of <pypiper.manager.PipelineManager object at 0x7fdffc7ee450>>
Traceback (most recent call last):
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2201, in _exit_handler
    self.fail_pipeline(Exception("Pipeline failure. See details above."))
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2045, in fail_pipeline
    raise exc
Exception: Pipeline failure. See details above.
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo0_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-15 20:37:29) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e3220166a77e53e0c1fbb4757fd0c8651e7bc9fc
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-15 09:28:29 -0500
*        Pipeline diff:  5 files changed, 54 insertions(+), 17 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo0


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo0
pipestat record identifier: demo0
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target exists: `/home/nsheff/code/seqcolapi/analysis/data/demo/demo0.fa.checksums`  
Traceback (most recent call last):
  File "/home/nsheff/code/seqcolapi/analysis/demo/../../seqcolapi/scconf.py", line 20, in getenv
    return os.environ[varname]
           ~~~~~~~~~~^^^^^^^^^
  File "<frozen os>", line 679, in __getitem__
KeyError: 'POSTGRES_DB'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py", line 78, in <module>
    pgdb = RDBDict()  # parameterized through env vars
           ^^^^^^^^^
  File "/home/nsheff/code/seqcolapi/analysis/demo/../../seqcolapi/scconf.py", line 89, in __init__
    self.db_name = db_name or getenv("POSTGRES_DB")
                              ^^^^^^^^^^^^^^^^^^^^^
  File "/home/nsheff/code/seqcolapi/analysis/demo/../../seqcolapi/scconf.py", line 22, in getenv
    raise Exception(f"Environment variable {varname} not set.")
Exception: Environment variable POSTGRES_DB not set.

### Pipeline failed at:  (02-15 20:37:29) elapsed: 0.0 _TIME_

Total time: 0:00:00
Failure reason: Pipeline failure. See details above.
Exception ignored in atexit callback: <bound method PipelineManager._exit_handler of <pypiper.manager.PipelineManager object at 0x7f6d2284d110>>
Traceback (most recent call last):
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2201, in _exit_handler
    self.fail_pipeline(Exception("Pipeline failure. See details above."))
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2045, in fail_pipeline
    raise exc
Exception: Pipeline failure. See details above.
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo0_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-15 20:37:49) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e3220166a77e53e0c1fbb4757fd0c8651e7bc9fc
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-15 09:28:29 -0500
*        Pipeline diff:  5 files changed, 54 insertions(+), 17 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo0


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo0
pipestat record identifier: demo0
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target exists: `/home/nsheff/code/seqcolapi/analysis/data/demo/demo0.fa.checksums`  
Traceback (most recent call last):
  File "/home/nsheff/code/seqcolapi/analysis/demo/../../seqcolapi/scconf.py", line 20, in getenv
    return os.environ[varname]
           ~~~~~~~~~~^^^^^^^^^
  File "<frozen os>", line 679, in __getitem__
KeyError: 'POSTGRES_DB'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py", line 78, in <module>
    pgdb = RDBDict()  # parameterized through env vars
           ^^^^^^^^^
  File "/home/nsheff/code/seqcolapi/analysis/demo/../../seqcolapi/scconf.py", line 89, in __init__
    self.db_name = db_name or getenv("POSTGRES_DB")
                              ^^^^^^^^^^^^^^^^^^^^^
  File "/home/nsheff/code/seqcolapi/analysis/demo/../../seqcolapi/scconf.py", line 22, in getenv
    raise Exception(f"Environment variable {varname} not set.")
Exception: Environment variable POSTGRES_DB not set.

### Pipeline failed at:  (02-15 20:37:49) elapsed: 0.0 _TIME_

Total time: 0:00:00
Failure reason: Pipeline failure. See details above.
Exception ignored in atexit callback: <bound method PipelineManager._exit_handler of <pypiper.manager.PipelineManager object at 0x7f9c2056c610>>
Traceback (most recent call last):
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2201, in _exit_handler
    self.fail_pipeline(Exception("Pipeline failure. See details above."))
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2045, in fail_pipeline
    raise exc
Exception: Pipeline failure. See details above.
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo0_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-15 20:39:59) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e3220166a77e53e0c1fbb4757fd0c8651e7bc9fc
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-15 09:28:29 -0500
*        Pipeline diff:  5 files changed, 54 insertions(+), 17 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo0


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo0
pipestat record identifier: demo0
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target exists: `/home/nsheff/code/seqcolapi/analysis/data/demo/demo0.fa.checksums`  
INFO 2024-02-15 20:39:59,285 | scconf:scconf:191 > Connection to PostgreSQL DB successful 
INFO 2024-02-15 20:39:59,285 | scconf:scconf:105 > <connection object at 0x7f5a529e34c0; dsn: 'user=seqcol_admin password=xxx dbname=seqcol host=databio-rds.c2i34ludgwj2.us-east-1.rds.amazonaws.com port=5432', closed: 0> 
INFO 2024-02-15 20:39:59,285 | yacman.yacman1:yacman1:626 > Could not locate seqcol config file. 
INFO 2024-02-15 20:39:59,285 | henge.henge:henge:49 > Reading URL: https://schema.databio.org/refget/SeqColArraySetInherent.yaml 
description: "SeqColArraySet"
type: object
henge_class: "SeqColArraySet"
properties:
  topologies:
    type: array
    henge_class: "strarray"
    items:
      type: string
      enum: ["circular", "linear"]
      default: "linear"  
  names:
    type: array
    henge_class: "strarray"
    items:
      type: string    
  lengths:
    type: array
    henge_class: "intarray"
    items:
      type: integer
  sequences:
    type: array
    henge_class: "seqarray"
    items:
      type: string
      henge_class: sequence
  sorted_name_length_pairs:
    type: array
    henge_class: "strarray"
    items:
      type: string
inherent:
  - names
  - lengths
  - sequences

INFO 2024-02-15 20:39:59,342 | refget.seqcol:seqcol:65 > Initializing SeqColHenge 
SeqColHenge: Henge object. Item types: SeqColArraySet,strarray,intarray,seqarray,sequence
Loading from chromsizes...
INFO 2024-02-15 20:39:59,395 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX 
INFO 2024-02-15 20:39:59,452 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX_item_type 
INFO 2024-02-15 20:39:59,476 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX_digest_version 
INFO 2024-02-15 20:39:59,511 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX_external_string 
INFO 2024-02-15 20:39:59,543 | scconf:scconf:168 > Updating existing value for Fw1r9eRxfOZD98KKrhlYQNEdSRHoVxAG 
INFO 2024-02-15 20:39:59,568 | scconf:scconf:168 > Updating existing value for Fw1r9eRxfOZD98KKrhlYQNEdSRHoVxAG_item_type 
INFO 2024-02-15 20:39:59,614 | scconf:scconf:168 > Updating existing value for Fw1r9eRxfOZD98KKrhlYQNEdSRHoVxAG_digest_version 
INFO 2024-02-15 20:39:59,641 | scconf:scconf:168 > Updating existing value for Fw1r9eRxfOZD98KKrhlYQNEdSRHoVxAG_external_string 
INFO 2024-02-15 20:39:59,671 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr 
INFO 2024-02-15 20:39:59,700 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr_item_type 
INFO 2024-02-15 20:39:59,729 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr_digest_version 
INFO 2024-02-15 20:39:59,756 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr_external_string 
INFO 2024-02-15 20:39:59,787 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z_ 
INFO 2024-02-15 20:39:59,817 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__item_type 
INFO 2024-02-15 20:39:59,842 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__digest_version 
INFO 2024-02-15 20:39:59,868 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__external_string 
INFO 2024-02-15 20:39:59,894 | scconf:scconf:168 > Updating existing value for fLf5M0BOIPIqcfbE6R8oYwxsy-PnoV32 
INFO 2024-02-15 20:39:59,919 | scconf:scconf:168 > Updating existing value for fLf5M0BOIPIqcfbE6R8oYwxsy-PnoV32_item_type 
INFO 2024-02-15 20:39:59,946 | scconf:scconf:168 > Updating existing value for fLf5M0BOIPIqcfbE6R8oYwxsy-PnoV32_digest_version 
INFO 2024-02-15 20:40:00,027 | scconf:scconf:168 > Updating existing value for fLf5M0BOIPIqcfbE6R8oYwxsy-PnoV32_external_string 

### Pipeline completed. Epilogue
*        Elapsed time (this run):  0:00:01
*  Total elapsed time (all runs):  0:00:00
*         Peak memory (this run):  0 GB
*        Pipeline completed time: 2024-02-15 20:40:00
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo1_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-15 20:40:00) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e3220166a77e53e0c1fbb4757fd0c8651e7bc9fc
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-15 09:28:29 -0500
*        Pipeline diff:  5 files changed, 54 insertions(+), 17 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo1


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo1
pipestat record identifier: demo1
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target exists: `/home/nsheff/code/seqcolapi/analysis/data/demo/demo1.fa.checksums`  
INFO 2024-02-15 20:40:01,028 | scconf:scconf:191 > Connection to PostgreSQL DB successful 
INFO 2024-02-15 20:40:01,029 | scconf:scconf:105 > <connection object at 0x7f057517b4c0; dsn: 'user=seqcol_admin password=xxx dbname=seqcol host=databio-rds.c2i34ludgwj2.us-east-1.rds.amazonaws.com port=5432', closed: 0> 
INFO 2024-02-15 20:40:01,029 | yacman.yacman1:yacman1:626 > Could not locate seqcol config file. 
INFO 2024-02-15 20:40:01,029 | henge.henge:henge:49 > Reading URL: https://schema.databio.org/refget/SeqColArraySetInherent.yaml 
description: "SeqColArraySet"
type: object
henge_class: "SeqColArraySet"
properties:
  topologies:
    type: array
    henge_class: "strarray"
    items:
      type: string
      enum: ["circular", "linear"]
      default: "linear"  
  names:
    type: array
    henge_class: "strarray"
    items:
      type: string    
  lengths:
    type: array
    henge_class: "intarray"
    items:
      type: integer
  sequences:
    type: array
    henge_class: "seqarray"
    items:
      type: string
      henge_class: sequence
  sorted_name_length_pairs:
    type: array
    henge_class: "strarray"
    items:
      type: string
inherent:
  - names
  - lengths
  - sequences

INFO 2024-02-15 20:40:01,079 | refget.seqcol:seqcol:65 > Initializing SeqColHenge 
SeqColHenge: Henge object. Item types: SeqColArraySet,strarray,intarray,seqarray,sequence
Loading from chromsizes...
INFO 2024-02-15 20:40:01,095 | scconf:scconf:168 > Updating existing value for cYSh9UjEuqglikl6SUw6IKjjuK0kKGVt 
INFO 2024-02-15 20:40:01,118 | scconf:scconf:168 > Updating existing value for cYSh9UjEuqglikl6SUw6IKjjuK0kKGVt_item_type 
INFO 2024-02-15 20:40:01,148 | scconf:scconf:168 > Updating existing value for cYSh9UjEuqglikl6SUw6IKjjuK0kKGVt_digest_version 
INFO 2024-02-15 20:40:01,178 | scconf:scconf:168 > Updating existing value for cYSh9UjEuqglikl6SUw6IKjjuK0kKGVt_external_string 
INFO 2024-02-15 20:40:01,206 | scconf:scconf:168 > Updating existing value for XEsH8IMZ09CBX17iXEWRagH50VGfARLo 
INFO 2024-02-15 20:40:01,234 | scconf:scconf:168 > Updating existing value for XEsH8IMZ09CBX17iXEWRagH50VGfARLo_item_type 
INFO 2024-02-15 20:40:01,272 | scconf:scconf:168 > Updating existing value for XEsH8IMZ09CBX17iXEWRagH50VGfARLo_digest_version 
INFO 2024-02-15 20:40:01,297 | scconf:scconf:168 > Updating existing value for XEsH8IMZ09CBX17iXEWRagH50VGfARLo_external_string 
INFO 2024-02-15 20:40:01,326 | scconf:scconf:168 > Updating existing value for VjYGGTzO5B6EehKtlsWCnXpNgHWns9vC 
INFO 2024-02-15 20:40:01,355 | scconf:scconf:168 > Updating existing value for VjYGGTzO5B6EehKtlsWCnXpNgHWns9vC_item_type 
INFO 2024-02-15 20:40:01,378 | scconf:scconf:168 > Updating existing value for VjYGGTzO5B6EehKtlsWCnXpNgHWns9vC_digest_version 
INFO 2024-02-15 20:40:01,402 | scconf:scconf:168 > Updating existing value for VjYGGTzO5B6EehKtlsWCnXpNgHWns9vC_external_string 
INFO 2024-02-15 20:40:01,488 | scconf:scconf:168 > Updating existing value for 5TK2xeaOB3WmheaDFTzE6G2zdStHNQCM 
INFO 2024-02-15 20:40:01,511 | scconf:scconf:168 > Updating existing value for 5TK2xeaOB3WmheaDFTzE6G2zdStHNQCM_item_type 
INFO 2024-02-15 20:40:01,539 | scconf:scconf:168 > Updating existing value for 5TK2xeaOB3WmheaDFTzE6G2zdStHNQCM_digest_version 
INFO 2024-02-15 20:40:01,577 | scconf:scconf:168 > Updating existing value for 5TK2xeaOB3WmheaDFTzE6G2zdStHNQCM_external_string 

### Pipeline completed. Epilogue
*        Elapsed time (this run):  0:00:01
*  Total elapsed time (all runs):  0:00:00
*         Peak memory (this run):  0 GB
*        Pipeline completed time: 2024-02-15 20:40:01
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo2_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-15 20:41:58) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e3220166a77e53e0c1fbb4757fd0c8651e7bc9fc
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-15 09:28:29 -0500
*        Pipeline diff:  5 files changed, 54 insertions(+), 17 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo2


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo2
pipestat record identifier: demo2
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target to produce: `/home/nsheff/code/seqcolapi/analysis/data/demo/demo2.fa.checksums`  

> `checksumseq --input /home/nsheff/code/seqcolapi/analysis/data/demo/demo2.fa --output /home/nsheff/code/seqcolapi/analysis/data/demo/demo2.fa.checksums` (56081)
<pre>
</pre>
Command completed. Elapsed time: 0:00:00. Running peak memory: 0GB.  
  PID: 56081;	Command: checksumseq;	Return code: 0;	Memory used: 0.0GB

INFO 2024-02-15 20:41:58,782 | scconf:scconf:191 > Connection to PostgreSQL DB successful 
INFO 2024-02-15 20:41:58,782 | scconf:scconf:105 > <connection object at 0x7f6ac55574c0; dsn: 'user=seqcol_admin password=xxx dbname=seqcol host=databio-rds.c2i34ludgwj2.us-east-1.rds.amazonaws.com port=5432', closed: 0> 
INFO 2024-02-15 20:41:58,782 | yacman.yacman1:yacman1:626 > Could not locate seqcol config file. 
INFO 2024-02-15 20:41:58,782 | henge.henge:henge:49 > Reading URL: https://schema.databio.org/refget/SeqColArraySetInherent.yaml 
description: "SeqColArraySet"
type: object
henge_class: "SeqColArraySet"
properties:
  topologies:
    type: array
    henge_class: "strarray"
    items:
      type: string
      enum: ["circular", "linear"]
      default: "linear"  
  names:
    type: array
    henge_class: "strarray"
    items:
      type: string    
  lengths:
    type: array
    henge_class: "intarray"
    items:
      type: integer
  sequences:
    type: array
    henge_class: "seqarray"
    items:
      type: string
      henge_class: sequence
  sorted_name_length_pairs:
    type: array
    henge_class: "strarray"
    items:
      type: string
inherent:
  - names
  - lengths
  - sequences

INFO 2024-02-15 20:41:58,850 | refget.seqcol:seqcol:65 > Initializing SeqColHenge 
SeqColHenge: Henge object. Item types: SeqColArraySet,strarray,intarray,seqarray,sequence
Loading from chromsizes...
INFO 2024-02-15 20:41:58,875 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp 
INFO 2024-02-15 20:41:58,911 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp_item_type 
INFO 2024-02-15 20:41:58,941 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp_digest_version 
INFO 2024-02-15 20:41:58,965 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp_external_string 
INFO 2024-02-15 20:41:58,993 | scconf:scconf:168 > Updating existing value for dOAOfPGkf3wAf3CUsbjVTKhY9Wq2DL6f 
INFO 2024-02-15 20:41:59,036 | scconf:scconf:168 > Updating existing value for dOAOfPGkf3wAf3CUsbjVTKhY9Wq2DL6f_item_type 
INFO 2024-02-15 20:41:59,065 | scconf:scconf:168 > Updating existing value for dOAOfPGkf3wAf3CUsbjVTKhY9Wq2DL6f_digest_version 
INFO 2024-02-15 20:41:59,093 | scconf:scconf:168 > Updating existing value for dOAOfPGkf3wAf3CUsbjVTKhY9Wq2DL6f_external_string 
INFO 2024-02-15 20:41:59,131 | scconf:scconf:168 > Updating existing value for jRkQnIS5K5k9WIkLxiJ0pvsPimKOM_ij 
INFO 2024-02-15 20:41:59,158 | scconf:scconf:168 > Updating existing value for jRkQnIS5K5k9WIkLxiJ0pvsPimKOM_ij_item_type 
INFO 2024-02-15 20:41:59,185 | scconf:scconf:168 > Updating existing value for jRkQnIS5K5k9WIkLxiJ0pvsPimKOM_ij_digest_version 
INFO 2024-02-15 20:41:59,220 | scconf:scconf:168 > Updating existing value for jRkQnIS5K5k9WIkLxiJ0pvsPimKOM_ij_external_string 
INFO 2024-02-15 20:41:59,249 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z_ 
INFO 2024-02-15 20:41:59,274 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__item_type 
INFO 2024-02-15 20:41:59,303 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__digest_version 
INFO 2024-02-15 20:41:59,335 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__external_string 
INFO 2024-02-15 20:41:59,366 | scconf:scconf:168 > Updating existing value for V7QPcpp5S1wYnPBmMGiO53LXRxr9tTQa 
INFO 2024-02-15 20:41:59,393 | scconf:scconf:168 > Updating existing value for V7QPcpp5S1wYnPBmMGiO53LXRxr9tTQa_item_type 
INFO 2024-02-15 20:41:59,424 | scconf:scconf:168 > Updating existing value for V7QPcpp5S1wYnPBmMGiO53LXRxr9tTQa_digest_version 
INFO 2024-02-15 20:41:59,449 | scconf:scconf:168 > Updating existing value for V7QPcpp5S1wYnPBmMGiO53LXRxr9tTQa_external_string 

### Pipeline completed. Epilogue
*        Elapsed time (this run):  0:00:01
*  Total elapsed time (all runs):  0:00:00
*         Peak memory (this run):  0 GB
*        Pipeline completed time: 2024-02-15 20:41:59
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo3_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-15 20:42:00) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e3220166a77e53e0c1fbb4757fd0c8651e7bc9fc
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-15 09:28:29 -0500
*        Pipeline diff:  5 files changed, 54 insertions(+), 17 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo3


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo3
pipestat record identifier: demo3
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target to produce: `/home/nsheff/code/seqcolapi/analysis/data/demo/demo3.fa.checksums`  

> `checksumseq --input /home/nsheff/code/seqcolapi/analysis/data/demo/demo3.fa --output /home/nsheff/code/seqcolapi/analysis/data/demo/demo3.fa.checksums` (56116)
<pre>
</pre>
Command completed. Elapsed time: 0:00:00. Running peak memory: 0GB.  
  PID: 56116;	Command: checksumseq;	Return code: 0;	Memory used: 0.0GB

INFO 2024-02-15 20:42:00,433 | scconf:scconf:191 > Connection to PostgreSQL DB successful 
INFO 2024-02-15 20:42:00,433 | scconf:scconf:105 > <connection object at 0x7f74610d74c0; dsn: 'user=seqcol_admin password=xxx dbname=seqcol host=databio-rds.c2i34ludgwj2.us-east-1.rds.amazonaws.com port=5432', closed: 0> 
INFO 2024-02-15 20:42:00,434 | yacman.yacman1:yacman1:626 > Could not locate seqcol config file. 
INFO 2024-02-15 20:42:00,434 | henge.henge:henge:49 > Reading URL: https://schema.databio.org/refget/SeqColArraySetInherent.yaml 
description: "SeqColArraySet"
type: object
henge_class: "SeqColArraySet"
properties:
  topologies:
    type: array
    henge_class: "strarray"
    items:
      type: string
      enum: ["circular", "linear"]
      default: "linear"  
  names:
    type: array
    henge_class: "strarray"
    items:
      type: string    
  lengths:
    type: array
    henge_class: "intarray"
    items:
      type: integer
  sequences:
    type: array
    henge_class: "seqarray"
    items:
      type: string
      henge_class: sequence
  sorted_name_length_pairs:
    type: array
    henge_class: "strarray"
    items:
      type: string
inherent:
  - names
  - lengths
  - sequences

INFO 2024-02-15 20:42:00,497 | refget.seqcol:seqcol:65 > Initializing SeqColHenge 
SeqColHenge: Henge object. Item types: SeqColArraySet,strarray,intarray,seqarray,sequence
Loading from chromsizes...
INFO 2024-02-15 20:42:00,516 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp 
INFO 2024-02-15 20:42:00,548 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp_item_type 
INFO 2024-02-15 20:42:00,572 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp_digest_version 
INFO 2024-02-15 20:42:00,598 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp_external_string 
INFO 2024-02-15 20:42:00,625 | scconf:scconf:168 > Updating existing value for xOOIQ4CMROo3yQ0VobUSVIwk1jikO4pq 
INFO 2024-02-15 20:42:00,653 | scconf:scconf:168 > Updating existing value for xOOIQ4CMROo3yQ0VobUSVIwk1jikO4pq_item_type 
INFO 2024-02-15 20:42:00,678 | scconf:scconf:168 > Updating existing value for xOOIQ4CMROo3yQ0VobUSVIwk1jikO4pq_digest_version 
INFO 2024-02-15 20:42:00,701 | scconf:scconf:168 > Updating existing value for xOOIQ4CMROo3yQ0VobUSVIwk1jikO4pq_external_string 
INFO 2024-02-15 20:42:00,728 | scconf:scconf:168 > Updating existing value for jRkQnIS5K5k9WIkLxiJ0pvsPimKOM_ij 
INFO 2024-02-15 20:42:00,764 | scconf:scconf:168 > Updating existing value for jRkQnIS5K5k9WIkLxiJ0pvsPimKOM_ij_item_type 
INFO 2024-02-15 20:42:00,788 | scconf:scconf:168 > Updating existing value for jRkQnIS5K5k9WIkLxiJ0pvsPimKOM_ij_digest_version 
INFO 2024-02-15 20:42:00,812 | scconf:scconf:168 > Updating existing value for jRkQnIS5K5k9WIkLxiJ0pvsPimKOM_ij_external_string 
INFO 2024-02-15 20:42:00,898 | scconf:scconf:168 > Updating existing value for _G-IybZWJOcCWYagm6qmjQTaRsKhNRT2 
INFO 2024-02-15 20:42:00,923 | scconf:scconf:168 > Updating existing value for _G-IybZWJOcCWYagm6qmjQTaRsKhNRT2_item_type 
INFO 2024-02-15 20:42:00,959 | scconf:scconf:168 > Updating existing value for _G-IybZWJOcCWYagm6qmjQTaRsKhNRT2_digest_version 
INFO 2024-02-15 20:42:00,983 | scconf:scconf:168 > Updating existing value for _G-IybZWJOcCWYagm6qmjQTaRsKhNRT2_external_string 

### Pipeline completed. Epilogue
*        Elapsed time (this run):  0:00:01
*  Total elapsed time (all runs):  0:00:00
*         Peak memory (this run):  0 GB
*        Pipeline completed time: 2024-02-15 20:42:01
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo4_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-15 20:42:01) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e3220166a77e53e0c1fbb4757fd0c8651e7bc9fc
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-15 09:28:29 -0500
*        Pipeline diff:  5 files changed, 54 insertions(+), 17 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo4


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo4
pipestat record identifier: demo4
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target to produce: `/home/nsheff/code/seqcolapi/analysis/data/demo/demo4.fa.checksums`  

> `checksumseq --input /home/nsheff/code/seqcolapi/analysis/data/demo/demo4.fa --output /home/nsheff/code/seqcolapi/analysis/data/demo/demo4.fa.checksums` (56151)
<pre>
</pre>
Command completed. Elapsed time: 0:00:00. Running peak memory: 0GB.  
  PID: 56151;	Command: checksumseq;	Return code: 0;	Memory used: 0.0GB

INFO 2024-02-15 20:42:01,994 | scconf:scconf:191 > Connection to PostgreSQL DB successful 
INFO 2024-02-15 20:42:01,994 | scconf:scconf:105 > <connection object at 0x7fb0f07ef4c0; dsn: 'user=seqcol_admin password=xxx dbname=seqcol host=databio-rds.c2i34ludgwj2.us-east-1.rds.amazonaws.com port=5432', closed: 0> 
INFO 2024-02-15 20:42:01,994 | yacman.yacman1:yacman1:626 > Could not locate seqcol config file. 
INFO 2024-02-15 20:42:01,994 | henge.henge:henge:49 > Reading URL: https://schema.databio.org/refget/SeqColArraySetInherent.yaml 
description: "SeqColArraySet"
type: object
henge_class: "SeqColArraySet"
properties:
  topologies:
    type: array
    henge_class: "strarray"
    items:
      type: string
      enum: ["circular", "linear"]
      default: "linear"  
  names:
    type: array
    henge_class: "strarray"
    items:
      type: string    
  lengths:
    type: array
    henge_class: "intarray"
    items:
      type: integer
  sequences:
    type: array
    henge_class: "seqarray"
    items:
      type: string
      henge_class: sequence
  sorted_name_length_pairs:
    type: array
    henge_class: "strarray"
    items:
      type: string
inherent:
  - names
  - lengths
  - sequences

INFO 2024-02-15 20:42:02,033 | refget.seqcol:seqcol:65 > Initializing SeqColHenge 
SeqColHenge: Henge object. Item types: SeqColArraySet,strarray,intarray,seqarray,sequence
Loading from chromsizes...
INFO 2024-02-15 20:42:02,049 | scconf:scconf:168 > Updating existing value for tT6ShOcWyUlHT1gqhYX9Jos9wStqtHBl 
INFO 2024-02-15 20:42:02,086 | scconf:scconf:168 > Updating existing value for tT6ShOcWyUlHT1gqhYX9Jos9wStqtHBl_item_type 
INFO 2024-02-15 20:42:02,111 | scconf:scconf:168 > Updating existing value for tT6ShOcWyUlHT1gqhYX9Jos9wStqtHBl_digest_version 
INFO 2024-02-15 20:42:02,139 | scconf:scconf:168 > Updating existing value for tT6ShOcWyUlHT1gqhYX9Jos9wStqtHBl_external_string 
INFO 2024-02-15 20:42:02,173 | scconf:scconf:168 > Updating existing value for RgMgL2OKPYdwokXug10nVlzEcwXFv0Pg 
INFO 2024-02-15 20:42:02,199 | scconf:scconf:168 > Updating existing value for RgMgL2OKPYdwokXug10nVlzEcwXFv0Pg_item_type 
INFO 2024-02-15 20:42:02,225 | scconf:scconf:168 > Updating existing value for RgMgL2OKPYdwokXug10nVlzEcwXFv0Pg_digest_version 
INFO 2024-02-15 20:42:02,249 | scconf:scconf:168 > Updating existing value for RgMgL2OKPYdwokXug10nVlzEcwXFv0Pg_external_string 
INFO 2024-02-15 20:42:02,276 | scconf:scconf:168 > Updating existing value for Qem3pJ27x7C6lAtmwtQcxBNIv0y9eqCF 
INFO 2024-02-15 20:42:02,302 | scconf:scconf:168 > Updating existing value for Qem3pJ27x7C6lAtmwtQcxBNIv0y9eqCF_item_type 
INFO 2024-02-15 20:42:02,328 | scconf:scconf:168 > Updating existing value for Qem3pJ27x7C6lAtmwtQcxBNIv0y9eqCF_digest_version 
INFO 2024-02-15 20:42:02,352 | scconf:scconf:168 > Updating existing value for Qem3pJ27x7C6lAtmwtQcxBNIv0y9eqCF_external_string 
INFO 2024-02-15 20:42:02,433 | scconf:scconf:168 > Updating existing value for D96Ze37DS8pG-jJXXjyHbUlb9coGht6g 
INFO 2024-02-15 20:42:02,459 | scconf:scconf:168 > Updating existing value for D96Ze37DS8pG-jJXXjyHbUlb9coGht6g_item_type 
INFO 2024-02-15 20:42:02,495 | scconf:scconf:168 > Updating existing value for D96Ze37DS8pG-jJXXjyHbUlb9coGht6g_digest_version 
INFO 2024-02-15 20:42:02,519 | scconf:scconf:168 > Updating existing value for D96Ze37DS8pG-jJXXjyHbUlb9coGht6g_external_string 

### Pipeline completed. Epilogue
*        Elapsed time (this run):  0:00:01
*  Total elapsed time (all runs):  0:00:00
*         Peak memory (this run):  0 GB
*        Pipeline completed time: 2024-02-15 20:42:02
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo5_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-15 20:42:03) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e3220166a77e53e0c1fbb4757fd0c8651e7bc9fc
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-15 09:28:29 -0500
*        Pipeline diff:  5 files changed, 54 insertions(+), 17 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo5


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo5
pipestat record identifier: demo5
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target to produce: `/home/nsheff/code/seqcolapi/analysis/data/demo/demo5.fa.checksums`  

> `checksumseq --input /home/nsheff/code/seqcolapi/analysis/data/demo/demo5.fa --output /home/nsheff/code/seqcolapi/analysis/data/demo/demo5.fa.checksums` (56186)
<pre>
</pre>
Command completed. Elapsed time: 0:00:00. Running peak memory: 0GB.  
  PID: 56186;	Command: checksumseq;	Return code: 0;	Memory used: 0.0GB

INFO 2024-02-15 20:42:03,504 | scconf:scconf:191 > Connection to PostgreSQL DB successful 
INFO 2024-02-15 20:42:03,504 | scconf:scconf:105 > <connection object at 0x7ff6ae4334c0; dsn: 'user=seqcol_admin password=xxx dbname=seqcol host=databio-rds.c2i34ludgwj2.us-east-1.rds.amazonaws.com port=5432', closed: 0> 
INFO 2024-02-15 20:42:03,505 | yacman.yacman1:yacman1:626 > Could not locate seqcol config file. 
INFO 2024-02-15 20:42:03,505 | henge.henge:henge:49 > Reading URL: https://schema.databio.org/refget/SeqColArraySetInherent.yaml 
description: "SeqColArraySet"
type: object
henge_class: "SeqColArraySet"
properties:
  topologies:
    type: array
    henge_class: "strarray"
    items:
      type: string
      enum: ["circular", "linear"]
      default: "linear"  
  names:
    type: array
    henge_class: "strarray"
    items:
      type: string    
  lengths:
    type: array
    henge_class: "intarray"
    items:
      type: integer
  sequences:
    type: array
    henge_class: "seqarray"
    items:
      type: string
      henge_class: sequence
  sorted_name_length_pairs:
    type: array
    henge_class: "strarray"
    items:
      type: string
inherent:
  - names
  - lengths
  - sequences

INFO 2024-02-15 20:42:03,556 | refget.seqcol:seqcol:65 > Initializing SeqColHenge 
SeqColHenge: Henge object. Item types: SeqColArraySet,strarray,intarray,seqarray,sequence
Loading from chromsizes...
INFO 2024-02-15 20:42:03,570 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp 
INFO 2024-02-15 20:42:03,596 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp_item_type 
INFO 2024-02-15 20:42:03,630 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp_digest_version 
INFO 2024-02-15 20:42:03,655 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp_external_string 
INFO 2024-02-15 20:42:03,680 | scconf:scconf:168 > Updating existing value for dOAOfPGkf3wAf3CUsbjVTKhY9Wq2DL6f 
INFO 2024-02-15 20:42:03,709 | scconf:scconf:168 > Updating existing value for dOAOfPGkf3wAf3CUsbjVTKhY9Wq2DL6f_item_type 
INFO 2024-02-15 20:42:03,747 | scconf:scconf:168 > Updating existing value for dOAOfPGkf3wAf3CUsbjVTKhY9Wq2DL6f_digest_version 
INFO 2024-02-15 20:42:03,774 | scconf:scconf:168 > Updating existing value for dOAOfPGkf3wAf3CUsbjVTKhY9Wq2DL6f_external_string 
INFO 2024-02-15 20:42:03,801 | scconf:scconf:168 > Updating existing value for 7t6Ulz6OeUWu6FBxntbvFKOl8w3icl2h 
INFO 2024-02-15 20:42:03,839 | scconf:scconf:168 > Updating existing value for 7t6Ulz6OeUWu6FBxntbvFKOl8w3icl2h_item_type 
INFO 2024-02-15 20:42:03,863 | scconf:scconf:168 > Updating existing value for 7t6Ulz6OeUWu6FBxntbvFKOl8w3icl2h_digest_version 
INFO 2024-02-15 20:42:03,888 | scconf:scconf:168 > Updating existing value for 7t6Ulz6OeUWu6FBxntbvFKOl8w3icl2h_external_string 
INFO 2024-02-15 20:42:03,915 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z_ 
INFO 2024-02-15 20:42:03,952 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__item_type 
INFO 2024-02-15 20:42:03,977 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__digest_version 
INFO 2024-02-15 20:42:04,004 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__external_string 
INFO 2024-02-15 20:42:04,044 | scconf:scconf:168 > Updating existing value for JPd9Y-hwnhGD7HPe3yka4Qtx2YsIL8tW 
INFO 2024-02-15 20:42:04,068 | scconf:scconf:168 > Updating existing value for JPd9Y-hwnhGD7HPe3yka4Qtx2YsIL8tW_item_type 
INFO 2024-02-15 20:42:04,092 | scconf:scconf:168 > Updating existing value for JPd9Y-hwnhGD7HPe3yka4Qtx2YsIL8tW_digest_version 
INFO 2024-02-15 20:42:04,118 | scconf:scconf:168 > Updating existing value for JPd9Y-hwnhGD7HPe3yka4Qtx2YsIL8tW_external_string 

### Pipeline completed. Epilogue
*        Elapsed time (this run):  0:00:01
*  Total elapsed time (all runs):  0:00:00
*         Peak memory (this run):  0 GB
*        Pipeline completed time: 2024-02-15 20:42:04
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo6_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-15 20:42:05) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e3220166a77e53e0c1fbb4757fd0c8651e7bc9fc
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-15 09:28:29 -0500
*        Pipeline diff:  5 files changed, 54 insertions(+), 17 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo6


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo6
pipestat record identifier: demo6
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target to produce: `/home/nsheff/code/seqcolapi/analysis/data/demo/demo6.fa.checksums`  

> `checksumseq --input /home/nsheff/code/seqcolapi/analysis/data/demo/demo6.fa --output /home/nsheff/code/seqcolapi/analysis/data/demo/demo6.fa.checksums` (56222)
<pre>
</pre>
Command completed. Elapsed time: 0:00:00. Running peak memory: 0GB.  
  PID: 56222;	Command: checksumseq;	Return code: 0;	Memory used: 0.0GB

INFO 2024-02-15 20:42:05,142 | scconf:scconf:191 > Connection to PostgreSQL DB successful 
INFO 2024-02-15 20:42:05,142 | scconf:scconf:105 > <connection object at 0x7fe238f0f4c0; dsn: 'user=seqcol_admin password=xxx dbname=seqcol host=databio-rds.c2i34ludgwj2.us-east-1.rds.amazonaws.com port=5432', closed: 0> 
INFO 2024-02-15 20:42:05,142 | yacman.yacman1:yacman1:626 > Could not locate seqcol config file. 
INFO 2024-02-15 20:42:05,142 | henge.henge:henge:49 > Reading URL: https://schema.databio.org/refget/SeqColArraySetInherent.yaml 
description: "SeqColArraySet"
type: object
henge_class: "SeqColArraySet"
properties:
  topologies:
    type: array
    henge_class: "strarray"
    items:
      type: string
      enum: ["circular", "linear"]
      default: "linear"  
  names:
    type: array
    henge_class: "strarray"
    items:
      type: string    
  lengths:
    type: array
    henge_class: "intarray"
    items:
      type: integer
  sequences:
    type: array
    henge_class: "seqarray"
    items:
      type: string
      henge_class: sequence
  sorted_name_length_pairs:
    type: array
    henge_class: "strarray"
    items:
      type: string
inherent:
  - names
  - lengths
  - sequences

INFO 2024-02-15 20:42:05,200 | refget.seqcol:seqcol:65 > Initializing SeqColHenge 
SeqColHenge: Henge object. Item types: SeqColArraySet,strarray,intarray,seqarray,sequence
Loading from chromsizes...
INFO 2024-02-15 20:42:05,214 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX 
INFO 2024-02-15 20:42:05,243 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX_item_type 
INFO 2024-02-15 20:42:05,290 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX_digest_version 
INFO 2024-02-15 20:42:05,314 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX_external_string 
INFO 2024-02-15 20:42:05,341 | scconf:scconf:168 > Updating existing value for Fw1r9eRxfOZD98KKrhlYQNEdSRHoVxAG 
INFO 2024-02-15 20:42:05,374 | scconf:scconf:168 > Updating existing value for Fw1r9eRxfOZD98KKrhlYQNEdSRHoVxAG_item_type 
INFO 2024-02-15 20:42:05,399 | scconf:scconf:168 > Updating existing value for Fw1r9eRxfOZD98KKrhlYQNEdSRHoVxAG_digest_version 
INFO 2024-02-15 20:42:05,422 | scconf:scconf:168 > Updating existing value for Fw1r9eRxfOZD98KKrhlYQNEdSRHoVxAG_external_string 
INFO 2024-02-15 20:42:05,448 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr 
INFO 2024-02-15 20:42:05,476 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr_item_type 
INFO 2024-02-15 20:42:05,501 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr_digest_version 
INFO 2024-02-15 20:42:05,524 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr_external_string 
INFO 2024-02-15 20:42:05,549 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z_ 
INFO 2024-02-15 20:42:05,580 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__item_type 
INFO 2024-02-15 20:42:05,604 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__digest_version 
INFO 2024-02-15 20:42:05,628 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__external_string 
INFO 2024-02-15 20:42:05,656 | scconf:scconf:168 > Updating existing value for fLf5M0BOIPIqcfbE6R8oYwxsy-PnoV32 
INFO 2024-02-15 20:42:05,691 | scconf:scconf:168 > Updating existing value for fLf5M0BOIPIqcfbE6R8oYwxsy-PnoV32_item_type 
INFO 2024-02-15 20:42:05,714 | scconf:scconf:168 > Updating existing value for fLf5M0BOIPIqcfbE6R8oYwxsy-PnoV32_digest_version 
INFO 2024-02-15 20:42:05,742 | scconf:scconf:168 > Updating existing value for fLf5M0BOIPIqcfbE6R8oYwxsy-PnoV32_external_string 

### Pipeline completed. Epilogue
*        Elapsed time (this run):  0:00:01
*  Total elapsed time (all runs):  0:00:00
*         Peak memory (this run):  0 GB
*        Pipeline completed time: 2024-02-15 20:42:05
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo4_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-17 07:23:20) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  c39bac871561302f3f8190c28fd939f14439e1c0
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-15 21:36:08 -0500
*        Pipeline diff:  4 files changed, 9 insertions(+), 3 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo4


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo4
pipestat record identifier: demo4
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target to produce: `/home/nsheff/code/seqcolapi/analysis/data/demo/demo4.fa.checksums`  

> `checksumseq --input /home/nsheff/code/seqcolapi/analysis/data/demo/demo4.fa --output /home/nsheff/code/seqcolapi/analysis/data/demo/demo4.fa.checksums` (8252)
<pre>
</pre>
Command completed. Elapsed time: 0:00:00. Running peak memory: 0GB.  
  PID: 8252;	Command: checksumseq;	Return code: 0;	Memory used: 0.0GB

Traceback (most recent call last):
  File "/home/nsheff/code/seqcolapi/analysis/demo/../../seqcolapi/scconf.py", line 20, in getenv
    return os.environ[varname]
           ~~~~~~~~~~^^^^^^^^^
  File "<frozen os>", line 679, in __getitem__
KeyError: 'POSTGRES_DB'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py", line 78, in <module>
    pgdb = RDBDict()  # parameterized through env vars
           ^^^^^^^^^
  File "/home/nsheff/code/seqcolapi/analysis/demo/../../seqcolapi/scconf.py", line 89, in __init__
    self.db_name = db_name or getenv("POSTGRES_DB")
                              ^^^^^^^^^^^^^^^^^^^^^
  File "/home/nsheff/code/seqcolapi/analysis/demo/../../seqcolapi/scconf.py", line 22, in getenv
    raise Exception(f"Environment variable {varname} not set.")
Exception: Environment variable POSTGRES_DB not set.

### Pipeline failed at:  (02-17 07:23:20) elapsed: 0.0 _TIME_

Total time: 0:00:00
Failure reason: Pipeline failure. See details above.
Exception ignored in atexit callback: <bound method PipelineManager._exit_handler of <pypiper.manager.PipelineManager object at 0x7f23968defd0>>
Traceback (most recent call last):
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2201, in _exit_handler
    self.fail_pipeline(Exception("Pipeline failure. See details above."))
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2045, in fail_pipeline
    raise exc
Exception: Pipeline failure. See details above.
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo4_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-17 07:24:47) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  c39bac871561302f3f8190c28fd939f14439e1c0
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-15 21:36:08 -0500
*        Pipeline diff:  6 files changed, 124 insertions(+), 4 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo4


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo4
pipestat record identifier: demo4
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target exists: `/home/nsheff/code/seqcolapi/analysis/data/demo/demo4.fa.checksums`  
INFO 2024-02-17 07:24:47,737 | scconf:scconf:191 > Connection to PostgreSQL DB successful 
INFO 2024-02-17 07:24:47,738 | scconf:scconf:105 > <connection object at 0x7fde0fdff4c0; dsn: 'user=seqcol_admin password=xxx dbname=seqcol host=databio-rds.c2i34ludgwj2.us-east-1.rds.amazonaws.com port=5432', closed: 0> 
INFO 2024-02-17 07:24:47,738 | yacman.yacman1:yacman1:626 > Could not locate seqcol config file. 
INFO 2024-02-17 07:24:47,738 | henge.henge:henge:50 > Reading URL: https://schema.databio.org/refget/SeqColArraySetInherent.yaml 
INFO 2024-02-17 07:24:47,866 | refget.seqcol:seqcol:65 > Initializing SeqColHenge 
SeqColHenge: Henge object. Item types: SeqColArraySet,strarray,intarray,seqarray,sequence
Loading from chromsizes...
INFO 2024-02-17 07:24:47,914 | scconf:scconf:168 > Updating existing value for tT6ShOcWyUlHT1gqhYX9Jos9wStqtHBl 
INFO 2024-02-17 07:24:47,949 | scconf:scconf:168 > Updating existing value for tT6ShOcWyUlHT1gqhYX9Jos9wStqtHBl_item_type 
INFO 2024-02-17 07:24:47,972 | scconf:scconf:168 > Updating existing value for tT6ShOcWyUlHT1gqhYX9Jos9wStqtHBl_digest_version 
INFO 2024-02-17 07:24:48,001 | scconf:scconf:168 > Updating existing value for tT6ShOcWyUlHT1gqhYX9Jos9wStqtHBl_external_string 
INFO 2024-02-17 07:24:48,027 | scconf:scconf:168 > Updating existing value for RgMgL2OKPYdwokXug10nVlzEcwXFv0Pg 
INFO 2024-02-17 07:24:48,054 | scconf:scconf:168 > Updating existing value for RgMgL2OKPYdwokXug10nVlzEcwXFv0Pg_item_type 
INFO 2024-02-17 07:24:48,088 | scconf:scconf:168 > Updating existing value for RgMgL2OKPYdwokXug10nVlzEcwXFv0Pg_digest_version 
INFO 2024-02-17 07:24:48,116 | scconf:scconf:168 > Updating existing value for RgMgL2OKPYdwokXug10nVlzEcwXFv0Pg_external_string 
INFO 2024-02-17 07:24:48,143 | scconf:scconf:168 > Updating existing value for Qem3pJ27x7C6lAtmwtQcxBNIv0y9eqCF 
INFO 2024-02-17 07:24:48,167 | scconf:scconf:168 > Updating existing value for Qem3pJ27x7C6lAtmwtQcxBNIv0y9eqCF_item_type 
INFO 2024-02-17 07:24:48,193 | scconf:scconf:168 > Updating existing value for Qem3pJ27x7C6lAtmwtQcxBNIv0y9eqCF_digest_version 
INFO 2024-02-17 07:24:48,219 | scconf:scconf:168 > Updating existing value for Qem3pJ27x7C6lAtmwtQcxBNIv0y9eqCF_external_string 
INFO 2024-02-17 07:24:48,245 | scconf:scconf:168 > Updating existing value for B2kTRHJbed0zMKerGK_fBc08Smiyyxis 
INFO 2024-02-17 07:24:48,331 | scconf:scconf:168 > Updating existing value for B2kTRHJbed0zMKerGK_fBc08Smiyyxis_item_type 
INFO 2024-02-17 07:24:48,361 | scconf:scconf:168 > Updating existing value for B2kTRHJbed0zMKerGK_fBc08Smiyyxis_digest_version 
INFO 2024-02-17 07:24:48,385 | scconf:scconf:168 > Updating existing value for B2kTRHJbed0zMKerGK_fBc08Smiyyxis_external_string 
INFO 2024-02-17 07:24:48,424 | scconf:scconf:168 > Updating existing value for D96Ze37DS8pG-jJXXjyHbUlb9coGht6g 
INFO 2024-02-17 07:24:48,449 | scconf:scconf:168 > Updating existing value for D96Ze37DS8pG-jJXXjyHbUlb9coGht6g_item_type 
INFO 2024-02-17 07:24:48,473 | scconf:scconf:168 > Updating existing value for D96Ze37DS8pG-jJXXjyHbUlb9coGht6g_digest_version 
INFO 2024-02-17 07:24:48,501 | scconf:scconf:168 > Updating existing value for D96Ze37DS8pG-jJXXjyHbUlb9coGht6g_external_string 
These results exist for 'demo4': seqcol_digest
These results exist for 'demo4': Time
These results exist for 'demo4': Success

### Pipeline completed. Epilogue
*        Elapsed time (this run):  0:00:01
*  Total elapsed time (all runs):  0:00:00
*         Peak memory (this run):  0 GB
*        Pipeline completed time: 2024-02-17 07:24:48
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo4_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-17 07:31:42) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  f651461a3d67d295b6762202e471840e36ab0912
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-17 07:26:50 -0500
*        Pipeline diff:  7 files changed, 232 insertions(+), 5 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo4


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo4
pipestat record identifier: demo4
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target to produce: `/home/nsheff/code/seqcolapi/analysis/data/demo/demo4.fa.checksums`  

> `checksumseq --input /home/nsheff/code/seqcolapi/analysis/data/demo/demo4.fa --output /home/nsheff/code/seqcolapi/analysis/data/demo/demo4.fa.checksums` (11896)
<pre>
</pre>
Command completed. Elapsed time: 0:00:00. Running peak memory: 0GB.  
  PID: 11896;	Command: checksumseq;	Return code: 0;	Memory used: 0.0GB

INFO 2024-02-17 07:31:42,253 | scconf:scconf:191 > Connection to PostgreSQL DB successful 
INFO 2024-02-17 07:31:42,253 | scconf:scconf:105 > <connection object at 0x7ff9499e34c0; dsn: 'user=seqcol_admin password=xxx dbname=seqcol host=databio-rds.c2i34ludgwj2.us-east-1.rds.amazonaws.com port=5432', closed: 0> 
INFO 2024-02-17 07:31:42,253 | yacman.yacman1:yacman1:626 > Could not locate seqcol config file. 
INFO 2024-02-17 07:31:42,253 | henge.henge:henge:50 > Reading URL: https://schema.databio.org/refget/SeqColArraySetInherent.yaml 
INFO 2024-02-17 07:31:42,334 | refget.seqcol:seqcol:65 > Initializing SeqColHenge 
SeqColHenge: Henge object. Item types: SeqColArraySet,strarray,intarray,seqarray,sequence
Loading from chromsizes...
INFO 2024-02-17 07:31:42,364 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp 
INFO 2024-02-17 07:31:42,392 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp_item_type 
INFO 2024-02-17 07:31:42,432 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp_digest_version 
INFO 2024-02-17 07:31:42,459 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp_external_string 
INFO 2024-02-17 07:31:42,551 | scconf:scconf:168 > Updating existing value for jRkQnIS5K5k9WIkLxiJ0pvsPimKOM_ij 
INFO 2024-02-17 07:31:42,579 | scconf:scconf:168 > Updating existing value for jRkQnIS5K5k9WIkLxiJ0pvsPimKOM_ij_item_type 
INFO 2024-02-17 07:31:42,606 | scconf:scconf:168 > Updating existing value for jRkQnIS5K5k9WIkLxiJ0pvsPimKOM_ij_digest_version 
INFO 2024-02-17 07:31:42,635 | scconf:scconf:168 > Updating existing value for jRkQnIS5K5k9WIkLxiJ0pvsPimKOM_ij_external_string 
INFO 2024-02-17 07:31:42,662 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z_ 
INFO 2024-02-17 07:31:42,686 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__item_type 
INFO 2024-02-17 07:31:42,711 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__digest_version 
INFO 2024-02-17 07:31:42,742 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__external_string 
These results exist for 'demo4': seqcol_digest
These results exist for 'demo4': Time
These results exist for 'demo4': Success

### Pipeline completed. Epilogue
*        Elapsed time (this run):  0:00:01
*  Total elapsed time (all runs):  0:00:00
*         Peak memory (this run):  0 GB
*        Pipeline completed time: 2024-02-17 07:31:42
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo4_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-17 07:40:51) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  f651461a3d67d295b6762202e471840e36ab0912
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-17 07:26:50 -0500
*        Pipeline diff:  8 files changed, 342 insertions(+), 10 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo4


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo4
pipestat record identifier: demo4
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target exists: `/home/nsheff/code/seqcolapi/analysis/data/demo/demo4.fa.checksums`  
INFO 2024-02-17 07:40:51,267 | scconf:scconf:191 > Connection to PostgreSQL DB successful 
INFO 2024-02-17 07:40:51,267 | scconf:scconf:105 > <connection object at 0x7fe46243b4c0; dsn: 'user=seqcol_admin password=xxx dbname=seqcol host=databio-rds.c2i34ludgwj2.us-east-1.rds.amazonaws.com port=5432', closed: 0> 
INFO 2024-02-17 07:40:51,267 | yacman.yacman1:yacman1:626 > Could not locate seqcol config file. 
INFO 2024-02-17 07:40:51,267 | henge.henge:henge:50 > Reading URL: https://schema.databio.org/refget/SeqColArraySetInherent.yaml 
INFO 2024-02-17 07:40:51,370 | refget.seqcol:seqcol:65 > Initializing SeqColHenge 
SeqColHenge: Henge object. Item types: SeqColArraySet,strarray,intarray,seqarray,sequence
Loading from chromsizes...
INFO 2024-02-17 07:40:51,412 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp 
INFO 2024-02-17 07:40:51,439 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp_item_type 
INFO 2024-02-17 07:40:51,465 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp_digest_version 
INFO 2024-02-17 07:40:51,490 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp_external_string 
INFO 2024-02-17 07:40:51,569 | scconf:scconf:168 > Updating existing value for gSWbV6khfIsnlQTyw1PmlQ8G7VRfIWbU 
INFO 2024-02-17 07:40:51,604 | scconf:scconf:168 > Updating existing value for gSWbV6khfIsnlQTyw1PmlQ8G7VRfIWbU_item_type 
INFO 2024-02-17 07:40:51,629 | scconf:scconf:168 > Updating existing value for gSWbV6khfIsnlQTyw1PmlQ8G7VRfIWbU_digest_version 
INFO 2024-02-17 07:40:51,661 | scconf:scconf:168 > Updating existing value for gSWbV6khfIsnlQTyw1PmlQ8G7VRfIWbU_external_string 
INFO 2024-02-17 07:40:51,690 | scconf:scconf:168 > Updating existing value for jRkQnIS5K5k9WIkLxiJ0pvsPimKOM_ij 
INFO 2024-02-17 07:40:51,741 | scconf:scconf:168 > Updating existing value for jRkQnIS5K5k9WIkLxiJ0pvsPimKOM_ij_item_type 
INFO 2024-02-17 07:40:51,765 | scconf:scconf:168 > Updating existing value for jRkQnIS5K5k9WIkLxiJ0pvsPimKOM_ij_digest_version 
INFO 2024-02-17 07:40:51,789 | scconf:scconf:168 > Updating existing value for jRkQnIS5K5k9WIkLxiJ0pvsPimKOM_ij_external_string 
INFO 2024-02-17 07:40:51,822 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z_ 
INFO 2024-02-17 07:40:51,846 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__item_type 
INFO 2024-02-17 07:40:51,871 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__digest_version 
INFO 2024-02-17 07:40:51,897 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__external_string 
INFO 2024-02-17 07:40:51,926 | scconf:scconf:168 > Updating existing value for fA00QeHT0S71LuhX_QBMWVFEEnijlHSm 
INFO 2024-02-17 07:40:51,950 | scconf:scconf:168 > Updating existing value for fA00QeHT0S71LuhX_QBMWVFEEnijlHSm_item_type 
INFO 2024-02-17 07:40:51,977 | scconf:scconf:168 > Updating existing value for fA00QeHT0S71LuhX_QBMWVFEEnijlHSm_digest_version 
INFO 2024-02-17 07:40:52,002 | scconf:scconf:168 > Updating existing value for fA00QeHT0S71LuhX_QBMWVFEEnijlHSm_external_string 

### Pipeline completed. Epilogue
*        Elapsed time (this run):  0:00:01
*  Total elapsed time (all runs):  0:00:00
*         Peak memory (this run):  0 GB
*        Pipeline completed time: 2024-02-17 07:40:52
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo4_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-17 08:19:33) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e125d017f720dc3645535d31e16a3cde12cb4898
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-17 07:43:47 -0500
*        Pipeline diff:  4 files changed, 40 insertions(+), 39 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo4


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo4
pipestat record identifier: demo4
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target exists: `/home/nsheff/code/seqcolapi/analysis/data/demo/demo4.fa.checksums`  
Traceback (most recent call last):
  File "/home/nsheff/code/seqcolapi/analysis/demo/../../seqcolapi/scconf.py", line 20, in getenv
    return os.environ[varname]
           ~~~~~~~~~~^^^^^^^^^
  File "<frozen os>", line 679, in __getitem__
KeyError: 'POSTGRES_DB'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py", line 78, in <module>
    pgdb = RDBDict()  # parameterized through env vars
           ^^^^^^^^^
  File "/home/nsheff/code/seqcolapi/analysis/demo/../../seqcolapi/scconf.py", line 89, in __init__
    self.db_name = db_name or getenv("POSTGRES_DB")
                              ^^^^^^^^^^^^^^^^^^^^^
  File "/home/nsheff/code/seqcolapi/analysis/demo/../../seqcolapi/scconf.py", line 22, in getenv
    raise Exception(f"Environment variable {varname} not set.")
Exception: Environment variable POSTGRES_DB not set.

### Pipeline failed at:  (02-17 08:19:33) elapsed: 0.0 _TIME_

Total time: 0:00:00
Failure reason: Pipeline failure. See details above.
Exception ignored in atexit callback: <bound method PipelineManager._exit_handler of <pypiper.manager.PipelineManager object at 0x7f87a8c95e90>>
Traceback (most recent call last):
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2201, in _exit_handler
    self.fail_pipeline(Exception("Pipeline failure. See details above."))
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2045, in fail_pipeline
    raise exc
Exception: Pipeline failure. See details above.
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo4_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-17 08:21:22) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e125d017f720dc3645535d31e16a3cde12cb4898
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-17 07:43:47 -0500
*        Pipeline diff:  7 files changed, 143 insertions(+), 40 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo4


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo4
pipestat record identifier: demo4
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target exists: `/home/nsheff/code/seqcolapi/analysis/data/demo/demo4.fa.checksums`  
INFO 2024-02-17 08:21:22,833 | scconf:scconf:191 > Connection to PostgreSQL DB successful 
INFO 2024-02-17 08:21:22,833 | scconf:scconf:105 > <connection object at 0x7fd2dba0b4c0; dsn: 'user=seqcol_admin password=xxx dbname=seqcol host=databio-rds.c2i34ludgwj2.us-east-1.rds.amazonaws.com port=5432', closed: 0> 
INFO 2024-02-17 08:21:22,833 | yacman.yacman1:yacman1:626 > Could not locate seqcol config file. 
INFO 2024-02-17 08:21:22,834 | henge.henge:henge:50 > Reading URL: https://schema.databio.org/refget/SeqColArraySetInherent.yaml 
INFO 2024-02-17 08:21:22,908 | refget.seqcol:seqcol:65 > Initializing SeqColHenge 
SeqColHenge: Henge object. Item types: SeqColArraySet,strarray,intarray,seqarray,sequence
Loading from chromsizes...
INFO 2024-02-17 08:21:22,935 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp 
INFO 2024-02-17 08:21:22,960 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp_item_type 
INFO 2024-02-17 08:21:22,984 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp_digest_version 
INFO 2024-02-17 08:21:23,019 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp_external_string 
INFO 2024-02-17 08:21:23,051 | scconf:scconf:168 > Updating existing value for gSWbV6khfIsnlQTyw1PmlQ8G7VRfIWbU 
INFO 2024-02-17 08:21:23,075 | scconf:scconf:168 > Updating existing value for gSWbV6khfIsnlQTyw1PmlQ8G7VRfIWbU_item_type 
INFO 2024-02-17 08:21:23,108 | scconf:scconf:168 > Updating existing value for gSWbV6khfIsnlQTyw1PmlQ8G7VRfIWbU_digest_version 
INFO 2024-02-17 08:21:23,134 | scconf:scconf:168 > Updating existing value for gSWbV6khfIsnlQTyw1PmlQ8G7VRfIWbU_external_string 
INFO 2024-02-17 08:21:23,161 | scconf:scconf:168 > Updating existing value for jRkQnIS5K5k9WIkLxiJ0pvsPimKOM_ij 
INFO 2024-02-17 08:21:23,186 | scconf:scconf:168 > Updating existing value for jRkQnIS5K5k9WIkLxiJ0pvsPimKOM_ij_item_type 
INFO 2024-02-17 08:21:23,211 | scconf:scconf:168 > Updating existing value for jRkQnIS5K5k9WIkLxiJ0pvsPimKOM_ij_digest_version 
INFO 2024-02-17 08:21:23,236 | scconf:scconf:168 > Updating existing value for jRkQnIS5K5k9WIkLxiJ0pvsPimKOM_ij_external_string 
INFO 2024-02-17 08:21:23,263 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z_ 
INFO 2024-02-17 08:21:23,287 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__item_type 
INFO 2024-02-17 08:21:23,316 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__digest_version 
INFO 2024-02-17 08:21:23,344 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__external_string 
INFO 2024-02-17 08:21:23,372 | scconf:scconf:168 > Updating existing value for fA00QeHT0S71LuhX_QBMWVFEEnijlHSm 
INFO 2024-02-17 08:21:23,399 | scconf:scconf:168 > Updating existing value for fA00QeHT0S71LuhX_QBMWVFEEnijlHSm_item_type 
INFO 2024-02-17 08:21:23,428 | scconf:scconf:168 > Updating existing value for fA00QeHT0S71LuhX_QBMWVFEEnijlHSm_digest_version 
INFO 2024-02-17 08:21:23,457 | scconf:scconf:168 > Updating existing value for fA00QeHT0S71LuhX_QBMWVFEEnijlHSm_external_string 
These results exist for 'demo4': seqcol_digest
These results exist for 'demo4': Time
These results exist for 'demo4': Success

### Pipeline completed. Epilogue
*        Elapsed time (this run):  0:00:01
*  Total elapsed time (all runs):  0:00:00
*         Peak memory (this run):  0 GB
*        Pipeline completed time: 2024-02-17 08:21:23
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/demo4_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-17 08:23:18) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e125d017f720dc3645535d31e16a3cde12cb4898
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-17 07:43:47 -0500
*        Pipeline diff:  7 files changed, 254 insertions(+), 39 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: demo4


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: demo4
pipestat record identifier: demo4
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target exists: `/home/nsheff/code/seqcolapi/analysis/data/demo/demo4.fa.checksums`  
INFO 2024-02-17 08:23:18,517 | scconf:scconf:191 > Connection to PostgreSQL DB successful 
INFO 2024-02-17 08:23:18,517 | scconf:scconf:105 > <connection object at 0x7fe4b24474c0; dsn: 'user=seqcol_admin password=xxx dbname=seqcol host=databio-rds.c2i34ludgwj2.us-east-1.rds.amazonaws.com port=5432', closed: 0> 
INFO 2024-02-17 08:23:18,517 | yacman.yacman1:yacman1:626 > Could not locate seqcol config file. 
INFO 2024-02-17 08:23:18,518 | henge.henge:henge:50 > Reading URL: https://schema.databio.org/refget/SeqColArraySetInherent.yaml 
INFO 2024-02-17 08:23:18,566 | refget.seqcol:seqcol:65 > Initializing SeqColHenge 
SeqColHenge: Henge object. Item types: SeqColArraySet,strarray,intarray,seqarray,sequence
Loading from chromsizes...
INFO 2024-02-17 08:23:18,588 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp 
INFO 2024-02-17 08:23:18,620 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp_item_type 
INFO 2024-02-17 08:23:18,649 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp_digest_version 
INFO 2024-02-17 08:23:18,673 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp_external_string 
INFO 2024-02-17 08:23:18,703 | scconf:scconf:168 > Updating existing value for gSWbV6khfIsnlQTyw1PmlQ8G7VRfIWbU 
INFO 2024-02-17 08:23:18,734 | scconf:scconf:168 > Updating existing value for gSWbV6khfIsnlQTyw1PmlQ8G7VRfIWbU_item_type 
INFO 2024-02-17 08:23:18,763 | scconf:scconf:168 > Updating existing value for gSWbV6khfIsnlQTyw1PmlQ8G7VRfIWbU_digest_version 
INFO 2024-02-17 08:23:18,787 | scconf:scconf:168 > Updating existing value for gSWbV6khfIsnlQTyw1PmlQ8G7VRfIWbU_external_string 
INFO 2024-02-17 08:23:18,821 | scconf:scconf:168 > Updating existing value for jRkQnIS5K5k9WIkLxiJ0pvsPimKOM_ij 
INFO 2024-02-17 08:23:18,845 | scconf:scconf:168 > Updating existing value for jRkQnIS5K5k9WIkLxiJ0pvsPimKOM_ij_item_type 
INFO 2024-02-17 08:23:18,871 | scconf:scconf:168 > Updating existing value for jRkQnIS5K5k9WIkLxiJ0pvsPimKOM_ij_digest_version 
INFO 2024-02-17 08:23:18,897 | scconf:scconf:168 > Updating existing value for jRkQnIS5K5k9WIkLxiJ0pvsPimKOM_ij_external_string 
INFO 2024-02-17 08:23:18,923 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z_ 
INFO 2024-02-17 08:23:18,951 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__item_type 
INFO 2024-02-17 08:23:18,974 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__digest_version 
INFO 2024-02-17 08:23:19,007 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__external_string 
INFO 2024-02-17 08:23:19,044 | scconf:scconf:168 > Updating existing value for fA00QeHT0S71LuhX_QBMWVFEEnijlHSm 
INFO 2024-02-17 08:23:19,079 | scconf:scconf:168 > Updating existing value for fA00QeHT0S71LuhX_QBMWVFEEnijlHSm_item_type 
INFO 2024-02-17 08:23:19,103 | scconf:scconf:168 > Updating existing value for fA00QeHT0S71LuhX_QBMWVFEEnijlHSm_digest_version 
INFO 2024-02-17 08:23:19,129 | scconf:scconf:168 > Updating existing value for fA00QeHT0S71LuhX_QBMWVFEEnijlHSm_external_string 
Final seqcol digest: fA00QeHT0S71LuhX_QBMWVFEEnijlHSm
{'chromsizes_file': '/home/nsheff/code/seqcolapi/analysis/data/demo/demo4.fa.checksums', 'SCAS': {'lengths': [4, 4, 8], 'names': ['chr2', 'chr1', 'chrX'], 'sequences': ['SQ.aKF498dAxcJAqme6QYQ7EZ07-fiw8Kw2', 'SQ.ORLd3OQy8whca09ypkTExMc_ByFalnnO', 'SQ.733WIVstq8gdCl6w8NhKc5sGdN6SZ5-I'], 'sorted_name_length_pairs': ['ESV_rcaJ-zgrfBr6sJ7J9kqldWX2gG_K', 'I0_AywNhq4XLlcc1vZexw5cHygCK_bLh', 'V2tENgwhEWrKc8UNgFzrMwx7H3JgoIuq']}, 'digest': 'fA00QeHT0S71LuhX_QBMWVFEEnijlHSm'}
These results exist for 'demo4': seqcol_digest
These results exist for 'demo4': Time
These results exist for 'demo4': Success

### Pipeline completed. Epilogue
*        Elapsed time (this run):  0:00:01
*  Total elapsed time (all runs):  0:00:00
*         Peak memory (this run):  0 GB
*        Pipeline completed time: 2024-02-17 08:23:19
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/base_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-17 08:43:11) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e125d017f720dc3645535d31e16a3cde12cb4898
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-17 07:43:47 -0500
*        Pipeline diff:  8 files changed, 367 insertions(+), 41 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: base


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: base
pipestat record identifier: base
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target to produce: `/home/nsheff/code/seqcolapi/analysis/data/test_data/base.fa.checksums`  

> `checksumseq --input /home/nsheff/code/seqcolapi/analysis/data/test_data/base.fa --output /home/nsheff/code/seqcolapi/analysis/data/test_data/base.fa.checksums` (16900)
<pre>
</pre>
Command completed. Elapsed time: 0:00:00. Running peak memory: 0GB.  
  PID: 16900;	Command: checksumseq;	Return code: 0;	Memory used: 0.0GB

INFO 2024-02-17 08:43:12,020 | scconf:scconf:191 > Connection to PostgreSQL DB successful 
INFO 2024-02-17 08:43:12,020 | scconf:scconf:105 > <connection object at 0x7fdf7b8fb4c0; dsn: 'user=seqcol_admin password=xxx dbname=seqcol host=databio-rds.c2i34ludgwj2.us-east-1.rds.amazonaws.com port=5432', closed: 0> 
INFO 2024-02-17 08:43:12,020 | yacman.yacman1:yacman1:626 > Could not locate seqcol config file. 
INFO 2024-02-17 08:43:12,020 | henge.henge:henge:50 > Reading URL: https://schema.databio.org/refget/SeqColArraySetInherent.yaml 
INFO 2024-02-17 08:43:12,102 | refget.seqcol:seqcol:65 > Initializing SeqColHenge 
SeqColHenge: Henge object. Item types: SeqColArraySet,strarray,intarray,seqarray,sequence
Loading from chromsizes...
INFO 2024-02-17 08:43:12,129 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX 
INFO 2024-02-17 08:43:12,158 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX_item_type 
INFO 2024-02-17 08:43:12,183 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX_digest_version 
INFO 2024-02-17 08:43:12,212 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX_external_string 
INFO 2024-02-17 08:43:12,238 | scconf:scconf:168 > Updating existing value for Fw1r9eRxfOZD98KKrhlYQNEdSRHoVxAG 
INFO 2024-02-17 08:43:12,271 | scconf:scconf:168 > Updating existing value for Fw1r9eRxfOZD98KKrhlYQNEdSRHoVxAG_item_type 
INFO 2024-02-17 08:43:12,302 | scconf:scconf:168 > Updating existing value for Fw1r9eRxfOZD98KKrhlYQNEdSRHoVxAG_digest_version 
INFO 2024-02-17 08:43:12,327 | scconf:scconf:168 > Updating existing value for Fw1r9eRxfOZD98KKrhlYQNEdSRHoVxAG_external_string 
INFO 2024-02-17 08:43:12,360 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr 
INFO 2024-02-17 08:43:12,385 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr_item_type 
INFO 2024-02-17 08:43:12,416 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr_digest_version 
INFO 2024-02-17 08:43:12,443 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr_external_string 
INFO 2024-02-17 08:43:12,475 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z_ 
INFO 2024-02-17 08:43:12,507 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__item_type 
INFO 2024-02-17 08:43:12,532 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__digest_version 
INFO 2024-02-17 08:43:12,558 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__external_string 
INFO 2024-02-17 08:43:12,587 | scconf:scconf:168 > Updating existing value for fLf5M0BOIPIqcfbE6R8oYwxsy-PnoV32 
INFO 2024-02-17 08:43:12,621 | scconf:scconf:168 > Updating existing value for fLf5M0BOIPIqcfbE6R8oYwxsy-PnoV32_item_type 
INFO 2024-02-17 08:43:12,648 | scconf:scconf:168 > Updating existing value for fLf5M0BOIPIqcfbE6R8oYwxsy-PnoV32_digest_version 
INFO 2024-02-17 08:43:12,681 | scconf:scconf:168 > Updating existing value for fLf5M0BOIPIqcfbE6R8oYwxsy-PnoV32_external_string 
Final seqcol digest: fLf5M0BOIPIqcfbE6R8oYwxsy-PnoV32
{'chromsizes_file': '/home/nsheff/code/seqcolapi/analysis/data/test_data/base.fa.checksums', 'SCAS': {'lengths': [8, 4, 4], 'names': ['chrX', 'chr1', 'chr2'], 'sequences': ['SQ.iYtREV555dUFKg2_agSJW6suquUyPpMw', 'SQ.YBbVX0dLKG1ieEDCiMmkrTZFt_Z5Vdaj', 'SQ.AcLxtBuKEPk_7PGE_H4dGElwZHCujwH6'], 'sorted_name_length_pairs': ['ESV_rcaJ-zgrfBr6sJ7J9kqldWX2gG_K', 'I0_AywNhq4XLlcc1vZexw5cHygCK_bLh', 'V2tENgwhEWrKc8UNgFzrMwx7H3JgoIuq']}, 'digest': 'fLf5M0BOIPIqcfbE6R8oYwxsy-PnoV32'}

### Pipeline completed. Epilogue
*        Elapsed time (this run):  0:00:01
*  Total elapsed time (all runs):  0:00:00
*         Peak memory (this run):  0 GB
*        Pipeline completed time: 2024-02-17 08:43:12
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/different_names_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-17 08:43:13) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e125d017f720dc3645535d31e16a3cde12cb4898
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-17 07:43:47 -0500
*        Pipeline diff:  9 files changed, 488 insertions(+), 41 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: different_names


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: different_names
pipestat record identifier: different_names
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target to produce: `/home/nsheff/code/seqcolapi/analysis/data/test_data/different_names.fa.checksums`  

> `checksumseq --input /home/nsheff/code/seqcolapi/analysis/data/test_data/different_names.fa --output /home/nsheff/code/seqcolapi/analysis/data/test_data/different_names.fa.checksums` (16937)
<pre>
</pre>
Command completed. Elapsed time: 0:00:00. Running peak memory: 0GB.  
  PID: 16937;	Command: checksumseq;	Return code: 0;	Memory used: 0.0GB

INFO 2024-02-17 08:43:13,715 | scconf:scconf:191 > Connection to PostgreSQL DB successful 
INFO 2024-02-17 08:43:13,715 | scconf:scconf:105 > <connection object at 0x7faa5a33b4c0; dsn: 'user=seqcol_admin password=xxx dbname=seqcol host=databio-rds.c2i34ludgwj2.us-east-1.rds.amazonaws.com port=5432', closed: 0> 
INFO 2024-02-17 08:43:13,715 | yacman.yacman1:yacman1:626 > Could not locate seqcol config file. 
INFO 2024-02-17 08:43:13,715 | henge.henge:henge:50 > Reading URL: https://schema.databio.org/refget/SeqColArraySetInherent.yaml 
INFO 2024-02-17 08:43:13,785 | refget.seqcol:seqcol:65 > Initializing SeqColHenge 
SeqColHenge: Henge object. Item types: SeqColArraySet,strarray,intarray,seqarray,sequence
Loading from chromsizes...
INFO 2024-02-17 08:43:13,799 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX 
INFO 2024-02-17 08:43:13,823 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX_item_type 
INFO 2024-02-17 08:43:13,850 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX_digest_version 
INFO 2024-02-17 08:43:13,874 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX_external_string 
INFO 2024-02-17 08:43:13,982 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr 
INFO 2024-02-17 08:43:14,012 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr_item_type 
INFO 2024-02-17 08:43:14,043 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr_digest_version 
INFO 2024-02-17 08:43:14,066 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr_external_string 
INFO 2024-02-17 08:43:14,093 | scconf:scconf:168 > Updating existing value for QdCffp8TyJbgkJh5lgvkRn7KkLiBw85A 
INFO 2024-02-17 08:43:14,116 | scconf:scconf:168 > Updating existing value for QdCffp8TyJbgkJh5lgvkRn7KkLiBw85A_item_type 
INFO 2024-02-17 08:43:14,145 | scconf:scconf:168 > Updating existing value for QdCffp8TyJbgkJh5lgvkRn7KkLiBw85A_digest_version 
INFO 2024-02-17 08:43:14,168 | scconf:scconf:168 > Updating existing value for QdCffp8TyJbgkJh5lgvkRn7KkLiBw85A_external_string 
Final seqcol digest: TKB7n_14iKSFjljBA-TSVjeYpxPQe0-k
{'chromsizes_file': '/home/nsheff/code/seqcolapi/analysis/data/test_data/different_names.fa.checksums', 'SCAS': {'lengths': [8, 4, 4], 'names': ['X', '1', '2'], 'sequences': ['SQ.iYtREV555dUFKg2_agSJW6suquUyPpMw', 'SQ.YBbVX0dLKG1ieEDCiMmkrTZFt_Z5Vdaj', 'SQ.AcLxtBuKEPk_7PGE_H4dGElwZHCujwH6'], 'sorted_name_length_pairs': ['FD2SCYHfvC0UE3PYFnavbAR3I76wtI5x', 'rkhUjVQn9nSaQ-FVrlxVBlc7nqifKvUk', 'zbEAQ7f3J3xyW-jWvzXeLKFc1qS-zh0h']}, 'digest': 'TKB7n_14iKSFjljBA-TSVjeYpxPQe0-k'}

### Pipeline completed. Epilogue
*        Elapsed time (this run):  0:00:01
*  Total elapsed time (all runs):  0:00:00
*         Peak memory (this run):  0 GB
*        Pipeline completed time: 2024-02-17 08:43:14
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/different_order_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-17 08:43:15) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e125d017f720dc3645535d31e16a3cde12cb4898
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-17 07:43:47 -0500
*        Pipeline diff:  9 files changed, 601 insertions(+), 41 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: different_order


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: different_order
pipestat record identifier: different_order
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target to produce: `/home/nsheff/code/seqcolapi/analysis/data/test_data/different_order.fa.checksums`  

> `checksumseq --input /home/nsheff/code/seqcolapi/analysis/data/test_data/different_order.fa --output /home/nsheff/code/seqcolapi/analysis/data/test_data/different_order.fa.checksums` (16973)
<pre>
</pre>
Command completed. Elapsed time: 0:00:00. Running peak memory: 0GB.  
  PID: 16973;	Command: checksumseq;	Return code: 0;	Memory used: 0.0GB

INFO 2024-02-17 08:43:15,298 | scconf:scconf:191 > Connection to PostgreSQL DB successful 
INFO 2024-02-17 08:43:15,299 | scconf:scconf:105 > <connection object at 0x7f0b7680f4c0; dsn: 'user=seqcol_admin password=xxx dbname=seqcol host=databio-rds.c2i34ludgwj2.us-east-1.rds.amazonaws.com port=5432', closed: 0> 
INFO 2024-02-17 08:43:15,299 | yacman.yacman1:yacman1:626 > Could not locate seqcol config file. 
INFO 2024-02-17 08:43:15,299 | henge.henge:henge:50 > Reading URL: https://schema.databio.org/refget/SeqColArraySetInherent.yaml 
INFO 2024-02-17 08:43:15,348 | refget.seqcol:seqcol:65 > Initializing SeqColHenge 
SeqColHenge: Henge object. Item types: SeqColArraySet,strarray,intarray,seqarray,sequence
Loading from chromsizes...
INFO 2024-02-17 08:43:15,362 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp 
INFO 2024-02-17 08:43:15,389 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp_item_type 
INFO 2024-02-17 08:43:15,420 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp_digest_version 
INFO 2024-02-17 08:43:15,455 | scconf:scconf:168 > Updating existing value for x5qpE4FtMkvlwpKIzvHs3a02Nex5tthp_external_string 
INFO 2024-02-17 08:43:15,493 | scconf:scconf:168 > Updating existing value for dOAOfPGkf3wAf3CUsbjVTKhY9Wq2DL6f 
INFO 2024-02-17 08:43:15,522 | scconf:scconf:168 > Updating existing value for dOAOfPGkf3wAf3CUsbjVTKhY9Wq2DL6f_item_type 
INFO 2024-02-17 08:43:15,546 | scconf:scconf:168 > Updating existing value for dOAOfPGkf3wAf3CUsbjVTKhY9Wq2DL6f_digest_version 
INFO 2024-02-17 08:43:15,582 | scconf:scconf:168 > Updating existing value for dOAOfPGkf3wAf3CUsbjVTKhY9Wq2DL6f_external_string 
INFO 2024-02-17 08:43:15,607 | scconf:scconf:168 > Updating existing value for 7t6Ulz6OeUWu6FBxntbvFKOl8w3icl2h 
INFO 2024-02-17 08:43:15,858 | scconf:scconf:168 > Updating existing value for 7t6Ulz6OeUWu6FBxntbvFKOl8w3icl2h_item_type 
INFO 2024-02-17 08:43:15,886 | scconf:scconf:168 > Updating existing value for 7t6Ulz6OeUWu6FBxntbvFKOl8w3icl2h_digest_version 
INFO 2024-02-17 08:43:15,910 | scconf:scconf:168 > Updating existing value for 7t6Ulz6OeUWu6FBxntbvFKOl8w3icl2h_external_string 
INFO 2024-02-17 08:43:15,938 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z_ 
INFO 2024-02-17 08:43:15,962 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__item_type 
INFO 2024-02-17 08:43:15,988 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__digest_version 
INFO 2024-02-17 08:43:16,013 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__external_string 
INFO 2024-02-17 08:43:16,044 | scconf:scconf:168 > Updating existing value for JPd9Y-hwnhGD7HPe3yka4Qtx2YsIL8tW 
INFO 2024-02-17 08:43:16,068 | scconf:scconf:168 > Updating existing value for JPd9Y-hwnhGD7HPe3yka4Qtx2YsIL8tW_item_type 
INFO 2024-02-17 08:43:16,091 | scconf:scconf:168 > Updating existing value for JPd9Y-hwnhGD7HPe3yka4Qtx2YsIL8tW_digest_version 
INFO 2024-02-17 08:43:16,115 | scconf:scconf:168 > Updating existing value for JPd9Y-hwnhGD7HPe3yka4Qtx2YsIL8tW_external_string 
Final seqcol digest: JPd9Y-hwnhGD7HPe3yka4Qtx2YsIL8tW
{'chromsizes_file': '/home/nsheff/code/seqcolapi/analysis/data/test_data/different_order.fa.checksums', 'SCAS': {'lengths': [4, 4, 8], 'names': ['chr1', 'chr2', 'chrX'], 'sequences': ['SQ.YBbVX0dLKG1ieEDCiMmkrTZFt_Z5Vdaj', 'SQ.AcLxtBuKEPk_7PGE_H4dGElwZHCujwH6', 'SQ.iYtREV555dUFKg2_agSJW6suquUyPpMw'], 'sorted_name_length_pairs': ['ESV_rcaJ-zgrfBr6sJ7J9kqldWX2gG_K', 'I0_AywNhq4XLlcc1vZexw5cHygCK_bLh', 'V2tENgwhEWrKc8UNgFzrMwx7H3JgoIuq']}, 'digest': 'JPd9Y-hwnhGD7HPe3yka4Qtx2YsIL8tW'}

### Pipeline completed. Epilogue
*        Elapsed time (this run):  0:00:01
*  Total elapsed time (all runs):  0:00:00
*         Peak memory (this run):  0 GB
*        Pipeline completed time: 2024-02-17 08:43:16
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/pair_swap_maintain_coords_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-17 08:43:17) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e125d017f720dc3645535d31e16a3cde12cb4898
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-17 07:43:47 -0500
*        Pipeline diff:  9 files changed, 722 insertions(+), 41 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: pair_swap_maintain_coords


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: pair_swap_maintain_coords
pipestat record identifier: pair_swap_maintain_coords
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target to produce: `/home/nsheff/code/seqcolapi/analysis/data/test_data/pair_swap_maintain_coords.fa.checksums`  

> `checksumseq --input /home/nsheff/code/seqcolapi/analysis/data/test_data/pair_swap_maintain_coords.fa --output /home/nsheff/code/seqcolapi/analysis/data/test_data/pair_swap_maintain_coords.fa.checksums` (17009)
<pre>
</pre>
Command completed. Elapsed time: 0:00:00. Running peak memory: 0GB.  
  PID: 17009;	Command: checksumseq;	Return code: 0;	Memory used: 0.0GB

INFO 2024-02-17 08:43:17,137 | scconf:scconf:191 > Connection to PostgreSQL DB successful 
INFO 2024-02-17 08:43:17,137 | scconf:scconf:105 > <connection object at 0x7f283dafb380; dsn: 'user=seqcol_admin password=xxx dbname=seqcol host=databio-rds.c2i34ludgwj2.us-east-1.rds.amazonaws.com port=5432', closed: 0> 
INFO 2024-02-17 08:43:17,137 | yacman.yacman1:yacman1:626 > Could not locate seqcol config file. 
INFO 2024-02-17 08:43:17,137 | henge.henge:henge:50 > Reading URL: https://schema.databio.org/refget/SeqColArraySetInherent.yaml 
INFO 2024-02-17 08:43:17,190 | refget.seqcol:seqcol:65 > Initializing SeqColHenge 
SeqColHenge: Henge object. Item types: SeqColArraySet,strarray,intarray,seqarray,sequence
Loading from chromsizes...
INFO 2024-02-17 08:43:17,205 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX 
INFO 2024-02-17 08:43:17,228 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX_item_type 
INFO 2024-02-17 08:43:17,253 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX_digest_version 
INFO 2024-02-17 08:43:17,285 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX_external_string 
INFO 2024-02-17 08:43:17,371 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr 
INFO 2024-02-17 08:43:17,446 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr_item_type 
INFO 2024-02-17 08:43:17,474 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr_digest_version 
INFO 2024-02-17 08:43:17,497 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr_external_string 
INFO 2024-02-17 08:43:17,524 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z_ 
INFO 2024-02-17 08:43:17,547 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__item_type 
INFO 2024-02-17 08:43:17,584 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__digest_version 
INFO 2024-02-17 08:43:17,607 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__external_string 
Final seqcol digest: EkMSPx-_MdAzj2tWGfdFSVsuv03OznPn
{'chromsizes_file': '/home/nsheff/code/seqcolapi/analysis/data/test_data/pair_swap_maintain_coords.fa.checksums', 'SCAS': {'lengths': [8, 4, 4], 'names': ['chrX', 'chr2', 'chr1'], 'sequences': ['SQ.iYtREV555dUFKg2_agSJW6suquUyPpMw', 'SQ.YBbVX0dLKG1ieEDCiMmkrTZFt_Z5Vdaj', 'SQ.AcLxtBuKEPk_7PGE_H4dGElwZHCujwH6'], 'sorted_name_length_pairs': ['ESV_rcaJ-zgrfBr6sJ7J9kqldWX2gG_K', 'I0_AywNhq4XLlcc1vZexw5cHygCK_bLh', 'V2tENgwhEWrKc8UNgFzrMwx7H3JgoIuq']}, 'digest': 'EkMSPx-_MdAzj2tWGfdFSVsuv03OznPn'}

### Pipeline completed. Epilogue
*        Elapsed time (this run):  0:00:01
*  Total elapsed time (all runs):  0:00:00
*         Peak memory (this run):  0 GB
*        Pipeline completed time: 2024-02-17 08:43:17
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/subset_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-17 08:43:18) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e125d017f720dc3645535d31e16a3cde12cb4898
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-17 07:43:47 -0500
*        Pipeline diff:  9 files changed, 835 insertions(+), 41 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: subset


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: subset
pipestat record identifier: subset
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target to produce: `/home/nsheff/code/seqcolapi/analysis/data/test_data/subset.fa.checksums`  

> `checksumseq --input /home/nsheff/code/seqcolapi/analysis/data/test_data/subset.fa --output /home/nsheff/code/seqcolapi/analysis/data/test_data/subset.fa.checksums` (17045)
<pre>
</pre>
Command completed. Elapsed time: 0:00:00. Running peak memory: 0GB.  
  PID: 17045;	Command: checksumseq;	Return code: 0;	Memory used: 0.0GB

INFO 2024-02-17 08:43:18,728 | scconf:scconf:191 > Connection to PostgreSQL DB successful 
INFO 2024-02-17 08:43:18,728 | scconf:scconf:105 > <connection object at 0x7f6abeb574c0; dsn: 'user=seqcol_admin password=xxx dbname=seqcol host=databio-rds.c2i34ludgwj2.us-east-1.rds.amazonaws.com port=5432', closed: 0> 
INFO 2024-02-17 08:43:18,728 | yacman.yacman1:yacman1:626 > Could not locate seqcol config file. 
INFO 2024-02-17 08:43:18,728 | henge.henge:henge:50 > Reading URL: https://schema.databio.org/refget/SeqColArraySetInherent.yaml 
INFO 2024-02-17 08:43:18,770 | refget.seqcol:seqcol:65 > Initializing SeqColHenge 
SeqColHenge: Henge object. Item types: SeqColArraySet,strarray,intarray,seqarray,sequence
Loading from chromsizes...
Final seqcol digest: 8aA37TYgiVohRqfRhXEeklIAXf2Rs8jw
{'chromsizes_file': '/home/nsheff/code/seqcolapi/analysis/data/test_data/subset.fa.checksums', 'SCAS': {'lengths': [8, 4], 'names': ['chrX', 'chr1'], 'sequences': ['SQ.iYtREV555dUFKg2_agSJW6suquUyPpMw', 'SQ.YBbVX0dLKG1ieEDCiMmkrTZFt_Z5Vdaj'], 'sorted_name_length_pairs': ['ESV_rcaJ-zgrfBr6sJ7J9kqldWX2gG_K', 'I0_AywNhq4XLlcc1vZexw5cHygCK_bLh']}, 'digest': '8aA37TYgiVohRqfRhXEeklIAXf2Rs8jw'}

### Pipeline completed. Epilogue
*        Elapsed time (this run):  0:00:01
*  Total elapsed time (all runs):  0:00:00
*         Peak memory (this run):  0 GB
*        Pipeline completed time: 2024-02-17 08:43:19
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/pair_swap_maintain_coords_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-17 08:55:55) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e125d017f720dc3645535d31e16a3cde12cb4898
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-17 07:43:47 -0500
*        Pipeline diff:  9 files changed, 936 insertions(+), 41 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: pair_swap_maintain_coords


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: pair_swap_maintain_coords
pipestat record identifier: pair_swap_maintain_coords
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target to produce: `/home/nsheff/code/seqcolapi/analysis/data/test_data/pair_swap_maintain_coords.fa.checksums`  

> `checksumseq --input /home/nsheff/code/seqcolapi/analysis/data/test_data/pair_swap_maintain_coords.fa --output /home/nsheff/code/seqcolapi/analysis/data/test_data/pair_swap_maintain_coords.fa.checksums` (17346)
<pre>
thread 'main' panicked at /home/nsheff/.cargo/registry/src/index.crates.io-6f17d22bba15001f/rust-gc-count-0.1.0/src/checksumseq.rs:47:41:
called `Result::unwrap()` on an `Err` value: Os { code: 2, kind: NotFound, message: "No such file or directory" }
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
</pre>
Command completed. Elapsed time: 0:00:00. Running peak memory: 0GB.  
  PID: 17346;	Command: checksumseq;	Return code: 101;	Memory used: 0.0GB


### Pipeline failed at:  (02-17 08:55:55) elapsed: 0.0 _TIME_

Total time: 0:00:00
Failure reason: Subprocess returned nonzero result. Check above output for details
Traceback (most recent call last):
  File "/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py", line 63, in <module>
    pm.run(command, target)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 1083, in run
    process_return_code, local_maxmem = self.callprint(
                                        ^^^^^^^^^^^^^^^
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 1352, in callprint
    self._triage_error(SubprocessError(msg), nofail)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2575, in _triage_error
    self.fail_pipeline(e)
  File "/home/nsheff/.local/lib/python3.11/site-packages/pypiper/manager.py", line 2045, in fail_pipeline
    raise exc
pypiper.exceptions.SubprocessError: Subprocess returned nonzero result. Check above output for details
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/swap_wo_coords_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-17 08:56:14) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e125d017f720dc3645535d31e16a3cde12cb4898
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-17 07:43:47 -0500
*        Pipeline diff:  9 files changed, 1037 insertions(+), 41 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: swap_wo_coords


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: swap_wo_coords
pipestat record identifier: swap_wo_coords
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target to produce: `/home/nsheff/code/seqcolapi/analysis/data/test_data/swap_wo_coords.fa.checksums`  

> `checksumseq --input /home/nsheff/code/seqcolapi/analysis/data/test_data/swap_wo_coords.fa --output /home/nsheff/code/seqcolapi/analysis/data/test_data/swap_wo_coords.fa.checksums` (17420)
<pre>
</pre>
Command completed. Elapsed time: 0:00:00. Running peak memory: 0GB.  
  PID: 17420;	Command: checksumseq;	Return code: 0;	Memory used: 0.0GB

INFO 2024-02-17 08:56:19,609 | scconf:scconf:191 > Connection to PostgreSQL DB successful 
INFO 2024-02-17 08:56:19,609 | scconf:scconf:105 > <connection object at 0x7fc37284b4c0; dsn: 'user=seqcol_admin password=xxx dbname=seqcol host=databio-rds.c2i34ludgwj2.us-east-1.rds.amazonaws.com port=5432', closed: 0> 
INFO 2024-02-17 08:56:19,609 | yacman.yacman1:yacman1:626 > Could not locate seqcol config file. 
INFO 2024-02-17 08:56:19,609 | henge.henge:henge:50 > Reading URL: https://schema.databio.org/refget/SeqColArraySetInherent.yaml 
INFO 2024-02-17 08:56:19,702 | refget.seqcol:seqcol:65 > Initializing SeqColHenge 
SeqColHenge: Henge object. Item types: SeqColArraySet,strarray,intarray,seqarray,sequence
Loading from chromsizes...
INFO 2024-02-17 08:56:19,725 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX 
INFO 2024-02-17 08:56:19,763 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX_item_type 
INFO 2024-02-17 08:56:19,789 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX_digest_version 
INFO 2024-02-17 08:56:19,823 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX_external_string 
INFO 2024-02-17 08:56:19,852 | scconf:scconf:168 > Updating existing value for QX5ur-faw5nXis8HXUK2kMxgY5MTGVRn 
INFO 2024-02-17 08:56:19,891 | scconf:scconf:168 > Updating existing value for QX5ur-faw5nXis8HXUK2kMxgY5MTGVRn_item_type 
INFO 2024-02-17 08:56:19,935 | scconf:scconf:168 > Updating existing value for QX5ur-faw5nXis8HXUK2kMxgY5MTGVRn_digest_version 
INFO 2024-02-17 08:56:19,967 | scconf:scconf:168 > Updating existing value for QX5ur-faw5nXis8HXUK2kMxgY5MTGVRn_external_string 
INFO 2024-02-17 08:56:19,997 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr 
INFO 2024-02-17 08:56:20,031 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr_item_type 
INFO 2024-02-17 08:56:20,056 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr_digest_version 
INFO 2024-02-17 08:56:20,082 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr_external_string 
INFO 2024-02-17 08:56:20,132 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z_ 
INFO 2024-02-17 08:56:20,156 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__item_type 
INFO 2024-02-17 08:56:20,184 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__digest_version 
INFO 2024-02-17 08:56:20,209 | scconf:scconf:168 > Updating existing value for EXmqru5BC4Nu8beq86XdCJrEb6jg6-Z__external_string 
INFO 2024-02-17 08:56:20,245 | scconf:scconf:168 > Updating existing value for EkMSPx-_MdAzj2tWGfdFSVsuv03OznPn 
INFO 2024-02-17 08:56:20,275 | scconf:scconf:168 > Updating existing value for EkMSPx-_MdAzj2tWGfdFSVsuv03OznPn_item_type 
INFO 2024-02-17 08:56:20,299 | scconf:scconf:168 > Updating existing value for EkMSPx-_MdAzj2tWGfdFSVsuv03OznPn_digest_version 
INFO 2024-02-17 08:56:20,403 | scconf:scconf:168 > Updating existing value for EkMSPx-_MdAzj2tWGfdFSVsuv03OznPn_external_string 
Final seqcol digest: EkMSPx-_MdAzj2tWGfdFSVsuv03OznPn
{'chromsizes_file': '/home/nsheff/code/seqcolapi/analysis/data/test_data/swap_wo_coords.fa.checksums', 'SCAS': {'lengths': [8, 4, 4], 'names': ['chrX', 'chr2', 'chr1'], 'sequences': ['SQ.iYtREV555dUFKg2_agSJW6suquUyPpMw', 'SQ.YBbVX0dLKG1ieEDCiMmkrTZFt_Z5Vdaj', 'SQ.AcLxtBuKEPk_7PGE_H4dGElwZHCujwH6'], 'sorted_name_length_pairs': ['ESV_rcaJ-zgrfBr6sJ7J9kqldWX2gG_K', 'I0_AywNhq4XLlcc1vZexw5cHygCK_bLh', 'V2tENgwhEWrKc8UNgFzrMwx7H3JgoIuq']}, 'digest': 'EkMSPx-_MdAzj2tWGfdFSVsuv03OznPn'}

### Pipeline completed. Epilogue
*        Elapsed time (this run):  0:00:06
*  Total elapsed time (all runs):  0:00:00
*         Peak memory (this run):  0 GB
*        Pipeline completed time: 2024-02-17 08:56:20
### Pipeline run code and environment:

*              Command:  `/home/nsheff/code/seqcolapi/analysis/demo/../pipeline/add_to_seqcol_server.py /home/nsheff/code/seqcolapi/analysis/demo/results/submission/pair_swap_sample.yaml /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml`
*         Compute host:  zither
*          Working dir:  /home/nsheff/code/seqcolapi/analysis/demo
*            Outfolder:  /home/nsheff/code/seqcolapi/analysis/demo/results/submission/
*  Pipeline started at:   (02-17 08:56:21) elapsed: 0.0 _TIME_

### Version log:

*       Python version:  3.11.7
*          Pypiper dir:  `/home/nsheff/.local/lib/python3.11/site-packages/pypiper`
*      Pypiper version:  0.14.0
*         Pipeline dir:  `/home/nsheff/code/seqcolapi/analysis/pipeline`
*     Pipeline version:  None
*        Pipeline hash:  e125d017f720dc3645535d31e16a3cde12cb4898
*      Pipeline branch:  * master
*        Pipeline date:  2024-02-17 07:43:47 -0500
*        Pipeline diff:  9 files changed, 1158 insertions(+), 41 deletions(-)

### Arguments passed to pipeline:


### Initialized Pipestat Object:

* PipestatManager (add_to_seqcol)
* Backend: File
*  - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
*  - status: /home/nsheff/code/seqcolapi/analysis/demo/results
* Multiple Pipelines Allowed: False
* Pipeline name: add_to_seqcol
* Pipeline type: sample
* Project Level Data:
* Sample Level Data:
*  seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
*  Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
*  Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
* Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
* Results formatter: default_formatter
* Results schema source: ../pipeline/output_schema.yaml
* Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
* Records count: 2
* Sample name: pair_swap


----------------------------------------

Pipestat manager name: add_to_seqcol
sample_name: pair_swap
pipestat record identifier: pair_swap
pipestat_results_file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
pipestat _file: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
PipestatManager (add_to_seqcol)
Backend: File
 - results: /home/nsheff/code/seqcolapi/analysis/demo/results/pipeline_stats.yaml
 - status: /home/nsheff/code/seqcolapi/analysis/demo/results
Multiple Pipelines Allowed: False
Pipeline name: add_to_seqcol
Pipeline type: sample
Project Level Data:
Sample Level Data:
 seqcol_digest : {'type': 'string', 'description': 'seqcol digest'}
 Time : {'type': 'string', 'description': 'Elapsed time for the pipeline run as reported by pypiper'}
 Success : {'type': 'string', 'description': 'Timestamp for when the pipeline completed'}
Status Schema key: {'running': {'description': 'the pipeline is running', 'color': [30, 144, 255]}, 'completed': {'description': 'the pipeline has completed', 'color': [50, 205, 50]}, 'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]}, 'waiting': {'description': 'the pipeline is waiting', 'color': [240, 230, 140]}, 'partial': {'description': 'the pipeline stopped before completion point', 'color': [169, 169, 169]}}
Results formatter: default_formatter
Results schema source: ../pipeline/output_schema.yaml
Status schema source: /home/nsheff/.local/lib/python3.11/site-packages/pipestat/schemas/status_schema.yaml
Records count: 2
Target to produce: `/home/nsheff/code/seqcolapi/analysis/data/test_data/pair_swap.fa.checksums`  

> `checksumseq --input /home/nsheff/code/seqcolapi/analysis/data/test_data/pair_swap.fa --output /home/nsheff/code/seqcolapi/analysis/data/test_data/pair_swap.fa.checksums` (17456)
<pre>
</pre>
Command completed. Elapsed time: 0:00:00. Running peak memory: 0GB.  
  PID: 17456;	Command: checksumseq;	Return code: 0;	Memory used: 0.0GB

INFO 2024-02-17 08:56:21,639 | scconf:scconf:191 > Connection to PostgreSQL DB successful 
INFO 2024-02-17 08:56:21,639 | scconf:scconf:105 > <connection object at 0x7eff40e2b4c0; dsn: 'user=seqcol_admin password=xxx dbname=seqcol host=databio-rds.c2i34ludgwj2.us-east-1.rds.amazonaws.com port=5432', closed: 0> 
INFO 2024-02-17 08:56:21,639 | yacman.yacman1:yacman1:626 > Could not locate seqcol config file. 
INFO 2024-02-17 08:56:21,639 | henge.henge:henge:50 > Reading URL: https://schema.databio.org/refget/SeqColArraySetInherent.yaml 
INFO 2024-02-17 08:56:21,686 | refget.seqcol:seqcol:65 > Initializing SeqColHenge 
SeqColHenge: Henge object. Item types: SeqColArraySet,strarray,intarray,seqarray,sequence
Loading from chromsizes...
INFO 2024-02-17 08:56:21,708 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX 
INFO 2024-02-17 08:56:21,732 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX_item_type 
INFO 2024-02-17 08:56:21,756 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX_digest_version 
INFO 2024-02-17 08:56:21,781 | scconf:scconf:168 > Updating existing value for cGRMZIb3AVgkcAfNv39RN7hnT5Chk7RX_external_string 
INFO 2024-02-17 08:56:21,811 | scconf:scconf:168 > Updating existing value for gSWbV6khfIsnlQTyw1PmlQ8G7VRfIWbU 
INFO 2024-02-17 08:56:21,835 | scconf:scconf:168 > Updating existing value for gSWbV6khfIsnlQTyw1PmlQ8G7VRfIWbU_item_type 
INFO 2024-02-17 08:56:21,859 | scconf:scconf:168 > Updating existing value for gSWbV6khfIsnlQTyw1PmlQ8G7VRfIWbU_digest_version 
INFO 2024-02-17 08:56:21,885 | scconf:scconf:168 > Updating existing value for gSWbV6khfIsnlQTyw1PmlQ8G7VRfIWbU_external_string 
INFO 2024-02-17 08:56:21,913 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr 
INFO 2024-02-17 08:56:21,936 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr_item_type 
INFO 2024-02-17 08:56:21,962 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr_digest_version 
INFO 2024-02-17 08:56:21,987 | scconf:scconf:168 > Updating existing value for 0uDQVLuHaOZi1u76LjV__yrVUIz9Bwhr_external_string 
Final seqcol digest: E6zGtGuc8wKYmCMw5gaLW3ppyXsoO6p4
{'chromsizes_file': '/home/nsheff/code/seqcolapi/analysis/data/test_data/pair_swap.fa.checksums', 'SCAS': {'lengths': [8, 4, 4], 'names': ['chr2', 'chr1', 'chrX'], 'sequences': ['SQ.iYtREV555dUFKg2_agSJW6suquUyPpMw', 'SQ.YBbVX0dLKG1ieEDCiMmkrTZFt_Z5Vdaj', 'SQ.AcLxtBuKEPk_7PGE_H4dGElwZHCujwH6'], 'sorted_name_length_pairs': ['I0_AywNhq4XLlcc1vZexw5cHygCK_bLh', 'XWyw5mz_6saiCzN4xFzz-D2oBbl_mdpl', '_Ksux7ic978gjc3FFWnqJdZFFgtUQZgt']}, 'digest': 'E6zGtGuc8wKYmCMw5gaLW3ppyXsoO6p4'}

### Pipeline completed. Epilogue
*        Elapsed time (this run):  0:00:01
*  Total elapsed time (all runs):  0:00:00
*         Peak memory (this run):  0 GB
*        Pipeline completed time: 2024-02-17 08:56:22
