# HPC-resources
In-depth resources for SLURM, HDFS, and Lustre

# Comprehensive HPC Cheat Sheet: SLURM, HDFS, and Lustre

This document serves as a quick reference guide for some of the most essential commands and configurations for SLURM (Simple Linux Utility for Resource Management), HDFS (Hadoop Distributed File System), and Lustre File System, widely used in high-performance computing (HPC) environments.

---

## SLURM Cheat Sheet

SLURM is an open-source, fault-tolerant, and highly scalable cluster management and job scheduling system for large and small Linux clusters.

### Basic Commands
- `sbatch script.sh`: Submit a batch job script.
- `squeue`: Display the status of jobs.
- `scancel job_id`: Cancel a job.
- `sinfo`: View information about nodes and partitions.

### Job Scheduling
- `srun --pty bash`: Run an interactive job.
- `sbatch --array=0-9 script.sh`: Submit a job array.

### Job Management
- `sacct -j job_id --format=JobID,JobName,MaxRSS,Elapsed`: Display detailed accounting data for a job.
- `scontrol show job job_id`: Show detailed information about a job.

### Advanced Features
- `salloc -N 2 -p partition_name --time=10:00`: Allocate resources for a job interactively.
- `scontrol update NodeName=node01 State=DOWN Reason=maintenance`: Update node state.

---

## HDFS Cheat Sheet

Hadoop Distributed File System (HDFS) is a distributed, scalable, and portable file system written in Java for the Hadoop framework.

### Basic File Operations
- `hdfs dfs -ls /path`: List files in a directory.
- `hdfs dfs -mkdir /path/dir`: Create a new directory.
- `hdfs dfs -put local_file /path`: Copy a file from the local filesystem to HDFS.

### Data Management
- `hdfs dfs -get /path/hdfs_file local_file`: Copy a file from HDFS to the local filesystem.
- `hdfs dfs -rm /path/file`: Delete a file.
- `hdfs dfs -cp /path/source /path/dest`: Copy file within HDFS.

### Cluster Information and Management
- `hdfs dfsadmin -report`: Report the status of HDFS.
- `hdfs fsck /path`: Check the health of HDFS files and directories.

---

## Lustre Cheat Sheet

Lustre is a type of parallel distributed file system, generally used for large-scale cluster computing.

### Basic File System Operations
- `lfs mkdir dirname`: Create a new directory in Lustre.
- `lfs getstripe filename`: Display stripe information of a file.

### Managing Data
- `lfs setstripe -c count filename`: Set stripe count for a file.
- `lfs find /path --size +size`: Find files larger than a specified size in Lustre.

### Performance Monitoring and Management
- `lfs df`: Display disk usage and availability in the file system.
- `ltop`: Real-time Lustre performance monitoring tool.
- `lctl get_param llite.*.read_ahead_stats`: Get read-ahead statistics for tuning.



