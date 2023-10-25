#!/bin/bash

PGDATA=$PWD/data/db
echo $PGDATA
mkdir -p $PGDATA

docker run -d \
    --name 'db' \
    -e POSTGRES_USER=jovyan \
    -e POSTGRES_PASSWORD=jovyan \
    -e PGDATA=/var/lib/postgresql/data/pgdata \
    -v $PGDATA:/var/lib/postgresql/data/pgdata \
    --network network_lmm \
    ankane/pgvector


