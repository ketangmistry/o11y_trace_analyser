from xmlrpc.client import boolean
from google.cloud.pubsublite import AdminClient
from google.api_core.exceptions import NotFound
from google.cloud.pubsublite.types import (
    CloudRegion,
    CloudZone,
    SubscriptionPath,
)


class Subscripton:
    project_no: str
    region: str
    zone_id: str
    pubsub_sub_id: str
    found: boolean = False


    def __init__(self, project_no, region, zone_id, pubsub_sub_id) -> None:
        self.project_no = project_no
        self.region = region
        self.zone_id = zone_id
        self.pubsub_sub_id = pubsub_sub_id


    def get_subscriptions(self):
        location = CloudZone(CloudRegion(self.region), self.zone_id)
        subscription_path = SubscriptionPath(self.project_no, location, self.pubsub_sub_id)

        client = AdminClient(self.region)
        try:
            response = client.get_subscription(subscription_path)
            self.found = True
        except NotFound:
            print(f'The {subscription_path} was not found.')

