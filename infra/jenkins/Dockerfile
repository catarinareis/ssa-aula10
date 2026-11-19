FROM docker:28-cli AS dockercli
FROM jenkins/jenkins:lts-jdk21
USER root
RUN apt-get update && apt-get install -y --no-install-recommends python3 git \
    && rm -rf /var/lib/apt/lists/*
COPY --from=dockercli /usr/local/bin/docker /usr/local/bin/docker
RUN mkdir -p /workspace && chown jenkins:jenkins /workspace
USER jenkins
RUN jenkins-plugin-cli --plugins workflow-aggregator git pipeline-stage-view pipeline-graph-view

