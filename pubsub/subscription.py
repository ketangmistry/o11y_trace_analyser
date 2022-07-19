from google.cloud.pubsublite.cloudpubsub import SubscriberClient
from google.cloud.pubsublite.types import (
    CloudRegion,
    CloudZone,
    SubscriptionPath,
)
from google.cloud.pubsublite.types import FlowControlSettings

class Subscripton:
    project_no: str
    region: str
    zone_id: str
    pubsub_sub_id: str
    response: str

    def __init__(self, project_no, region, zone_id, pubsub_sub_id) -> None:
        self.project_no = project_no
        self.region = region
        self.zone_id = zone_id
        self.pubsub_sub_id = pubsub_sub_id

    def get_trace_subscription(self):
        location = CloudZone(CloudRegion(self.region), self.zone_id)
        subscription_path = SubscriptionPath(self.project_no, location, self.pubsub_sub_id)

        managable_flow = FlowControlSettings(messages_outstanding=100, bytes_outstanding=1024)

        with SubscriberClient() as subscriber_client:
            streaming_pull_future = subscriber_client.subscribe(
                subscription_path,
                callback=self.callback,
                flow_control_settings = managable_flow
            )

            streaming_pull_future.result()

    def callback(self, message):
        self.response =  message.data.decode("utf-8")
        message.ack()
