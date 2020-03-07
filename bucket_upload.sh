#!/bin/bash
source env.sh 

aws s3 cp download/ $S3_BUCKET  --recursive --acl public-read

echo "files upload done"