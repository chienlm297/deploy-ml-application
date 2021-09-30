# Minio docs

To test Minio storage, open your terminal and run the command line `docker-compose up`

if it has no error you will see

```bash
Starting minio_minio_1 ... done
Attaching to minio_minio_1
minio_1  | WARNING: MINIO_ACCESS_KEY and MINIO_SECRET_KEY are deprecated.
minio_1  |          Please use MINIO_ROOT_USER and MINIO_ROOT_PASSWORD
minio_1  | 
minio_1  |  You are running an older version of MinIO released 1 month ago 
minio_1  |  Update: Run `mc admin update` 
minio_1  | 
minio_1  | 
minio_1  | API: http://172.18.0.2:9000  http://127.0.0.1:9000 
minio_1  | 
minio_1  | Console: http://172.18.0.2:35633 http://127.0.0.1:35633 
minio_1  | 
minio_1  | Documentation: https://docs.min.io
```

Go to [http://172.18.0.2:35633](http://172.18.0.2:35633) or [http://localhost:35633](http://localhost:35633) you will see the login page. Enter the user name and password to login.

Note that user and password are defined in
[docker-compose.yml](./docker-compose.yml)

```yaml
environment:
    - MINIO_ACCESS_KEY=${MINIO_SECRET_KEY:-minio-access-key}
    - MINIO_SECRET_KEY=${MINIO_SECRET_KEY:-minio-secret-key}
```

In this case, the user is **minio-access-key** and password is **minio-secret-key**

