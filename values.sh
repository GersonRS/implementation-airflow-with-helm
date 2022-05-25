export RELEASE_NAME=airflow # set a name!
export NAMESPACE=default # set a namespace!
export CHART_VERSION=8.6.0 # set a version!
export VALUES_FILE=./values.yaml # set your values file path!

# Helm 3
helm upgrade --install \
  $RELEASE_NAME \
  airflow-helm/airflow \
  --namespace $NAMESPACE \
  --create-namespace \
  --version $CHART_VERSION \
  --values $VALUES_FILE