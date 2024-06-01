'''
input data is in form of:
{
	'annie': {
		 'sue': {
			 'pizza': None,
			 'chicken': {
				 'charles': {
					 'bobby': None
				 }
			 }
		}
        'mark': {
            'jones': {
                'shirley': None
            }
        }
	},
	'bob': None
}

write a function that gets me the type: manager/ic, direct_reports, total_reports and produces this data model:
{
	annie: {type: 'manager', direct: 1, total: 5},
	bob: {type: 'ic', direct: 0,total: 0}
}
'''

ORG_CHART =  {
    'annie': {
        'sue': {
            'pizza': None,
            'chicken': {
                'charles': {
                    'bobby': None,
                    'derek': {
                        'eva': None
                    }
                }
            }
        },
        'mark': {
            'jones': {
                'shirley': None,
                'tina': {
                    'mike': None
                }
            }
        }
    },
    'bob': None,
    'claire': {
        'diana': None,
        'edward': {
            'francis': {
                'george': None,
                'harry': {
                    'ian': None
                }
            }
        }
    },
    'julia': {
        'karen': None,
        'larry': {
            'mary': {
                'nathan': None
            }
        }
    },
    'nancy': {
        'oliver': None,
        'paul': {
            'quincy': None,
            'rachel': {
                'steve': None
            }
        }
    }
}

class OrgManager:
    def __init__(self, org_chart):
        def helper(node, name):
            if not isinstance(node, dict) or len(node.keys()) == 0:
                self.result[name] = {'type': 'ic', 'directs': 0, 'total': 0 }
                return { 'type': 'ic', 'directs': 0, 'total': 0 }
            direct = len(node.keys())
            total = 0
            for child_name, child_node in node.items():
                reports = helper(child_node, child_name)
                total += 1 + reports['total']

            self.result[name] = { 'type': 'manager', 'total': total, 'directs': direct }
            return self.result[name]



        self.result = {}
        for name in org_chart.keys():
            reports = helper(org_chart[name], name)
            self.result[name] = {
                'type': 'manager' if reports['directs'] > 0 else 'ic',
                'direct': reports['directs'],
                'total': reports['total']
            }
        print(self.result)

OrgManager(ORG_CHART)
ORG_CHART = {
	'annie': {
	    'sue': {
			'pizza': None,
			'chicken': {
				'charles': {
					 'bobby': None
				}
			}
		}
	},
	'bob': None
}
# OrgManager(ORG_CHART)


