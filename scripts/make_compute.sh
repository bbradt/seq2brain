

aws batch create-job-queue --job-queue-name highPriority --compute-environment-order order=0,computeEnvironment=giftdocker-service  --priority 1000 --state ENABLED