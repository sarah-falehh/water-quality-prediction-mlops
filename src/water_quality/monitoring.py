from datetime import datetime, timezone
import logging

from elasticsearch import Elasticsearch

from .config import ELASTICSEARCH_URL

LOGGER = logging.getLogger(__name__)
INDEX_NAME = "mlops-metrics"


def log_metric(run_id: str, metric_name: str, value: float) -> None:
    """Send a metric to Elasticsearch without breaking the ML pipeline on failure."""
    try:
        client = Elasticsearch(ELASTICSEARCH_URL, request_timeout=3)
        client.index(
            index=INDEX_NAME,
            document={
                "run_id": run_id,
                "metric": metric_name,
                "value": float(value),
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "source": "water-quality-mlops-pipeline",
            },
        )
    except Exception as exc:  # monitoring must not stop training
        LOGGER.warning("Elasticsearch metric logging skipped: %s", exc)
