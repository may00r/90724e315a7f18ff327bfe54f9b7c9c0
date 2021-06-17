from celery import shared_task
from py_expression_eval import Parser
from django.conf import settings
import os
import requests


@shared_task
def get_chart(func, interval, dt, id):
    """Setting chart image

    Args:
        func ([str]): Function from db
        interval ([int]): Interval in days
        dt ([int]): Step in hours
        id ([int]): Function's id

    Returns:
        [str]: Returns chart image's path or error.
    """
    try:
        parser = Parser()
        func = func
        step = dt
        interval = interval
        x = [x for x in range(0+step, interval*24+step, step)]  # Generate xAxis
        y = [parser.parse(func).evaluate({'t': t}) for t in x]  # Generate yAxis

        url = "http://highcharts:8080/"

        data = {
            "infile": {
                    "title": {"text": "Steep Chart"},
                    "xAxis": {"categories": x},
                    "series": [{"data": y}]
            }
        }

        answer = requests.post(url, json=data)

        print(answer)

        file_path = '{}/media/chart_pics/'.format(settings.BASE_DIR)
        file_name = "chart_{}.png".format(id)
        completeName = os.path.join(file_path, file_name)
        file = open(completeName, "wb")
        file.write(answer.content)
        file.close()

        return ('/chart_pics/{}'.format(file_name))

    except Exception as e:
        return str(e)
