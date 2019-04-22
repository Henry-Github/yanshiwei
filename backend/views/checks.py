from flask_restful import Resource, reqparse
from algorithm_source import *
from typing import List
import json


class Checks(Resource):
    def get(self):
        parse = reqparse.RequestParser()
        parse.add_argument('name', type=str)
        parse.add_argument('methods', type=str)
        args = parse.parse_args()
        name = args.get('name')
        methods = json.loads(args.get('methods'))
        if name == 'check_1':
            names, scores, ranks = check_1_spot(methods)
            return {
                'status': 'Successful',
                'names': json.dumps(names),
                'scores': json.dumps(scores),
                'ranks': json.dumps(ranks)
            }
        elif name == 'check_2':
            names, scores, ranks = check_2_spot(methods)
            return {
                'status': 'Successful',
                'names': json.dumps(names),
                'scores': json.dumps(scores),
                'ranks': json.dumps(ranks)
            }
        elif name == 'check_3':
            names, scores, ranks = check_3_spot(methods)
            return {
                'status': 'Successful',
                'names': json.dumps(names),
                'scores': json.dumps(scores),
                'ranks': json.dumps(ranks)
            }
        elif name == 'check_4':
            names, scores, ranks = check_4_spot(methods)
            return {
                'status': 'Successful',
                'names': json.dumps(names),
                'scores': json.dumps(scores),
                'ranks': json.dumps(ranks)
            }
        elif name == 'check_5':
            names, scores, ranks = check_5_spot(methods)
            return {
                'status': 'Successful',
                'names': json.dumps(names),
                'scores': json.dumps(scores),
                'ranks': json.dumps(ranks)
            }
        else:
            pass
