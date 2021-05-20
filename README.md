##Pragma for GPU, awesome #OpemMP offloading! giving ~50X boost to LULESH! 

## Other [takeaways](https://twitter.com/animesh1977/status/1395375305544638467?s=20 ) - from openbas hpc workshop:
- Always Matrix ROW wise to exploit cache/forward seek
- collapse(#nest) PRAGMA for nested loops
- omp do(guided) as dynamic
- LCG_random is threadsafe
- decorate python functions with #numbas's @njit(parallel=True) with prange
- openMPI_ ALLREDUCE includes broadcasting
- SLURM --ntasks for MPI as #TOTAL process [script generatator](https://user.cscs.ch/access/running/jobscript_generator/ )
- lscpu / numactl --hardware // lstopo

