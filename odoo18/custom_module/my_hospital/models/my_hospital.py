from odoo import models, fields, api


class MyHospital(models.Model):
    _name = "my.hospital"
    _description = "Patient List"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    city = fields.Text(string="City")
    date = fields.Date(string="Date")
    condition = fields.Selection([
        ('bad', 'Bad'),
        ('good', 'Good')
    ], string="Patient Condition")

    # Reporting keliye hain. dhyan rahe
    def print_report(self):
        return self.env.ref('my_hospital.action_hospital_report').report_action(self)


# user_id = fields.Many2one("social.user")                       # Many posts → One user
# comment_ids = fields.One2many("social.comment", "post_id")     # One post → Many comments
# tag_ids = fields.Many2many("social.tag")                       # Many posts ↔ Many tags

# __ ORM __

# create, write, unnlink, copy, default get, name_create, search_count
# name_search, read(dict returns), fields_get(), exists(), ensure_one, get_metadata()
# filtered(), mapped(), sorted(),

# Lemme Overrite MyHospital class

# def create(self,vals):
#     print(vals)
#     rtn = super(MyHospital, self).create(vals)
#     print(rtn)
#     return rtn

# @api.model   # ( single dictionary only )
@api.model_create_multi  # (list of dictionary as many items)
def create(self, vals):
    print(self)
    print(vals)
    # rtn = super(MyHospital,self).create(vals)
    rtn = super().create(vals)  # This Also Works
    print(rtn)
    return rtn


def custom_method(self):
    data = {'patient_id': '2345',
            "name": "Test Hospital",
            'description': 'hello',
            'city': 'pune',
            'date': '1992-12-12',
            'condition': 'bad',
            }

    self.env["my.hospital"].create(data)


def write(self, vals):
    print(self)
    print(vals)
    rtn = super(MyHospital, self).write(vals)
    print(rtn)
    return rtn


def duplicate_records(self):
    print(self)
    duplicate_record = self.copy()
    print(duplicate_record)


def delete_records(self):
    records = self.env['my.hospital'].search([])  # Fetch all records
    for record in records:
        if not record.exists():
            print("Records not exists")
        else:
            records.unlink()  # Delete found records
            print(f"Deleted {len(records)} records")

    # if records:
    #     records.unlink()  # Delete found records
    #     print(f"Deleted {len(records)} records")
    # else:
    #     print("No records found to delete")


## SEARCH
def searchh(self):
    print("this is search feature")
    # search [domain, limit, offset, order]
    # [condition, more condition]
    # (field Name, operator, value ) <---- condition 1

    print(self.search([("name", 'ilike', "amit")]))
    # offset, order,


def unlink(self):
    print(self)
    rtn = super(MyHospital, self).unlink()
    print("unlinking method logix finish")
    return rtn


# return    Data
def custom_read(self):
    #  self.read_group( domain,
    #                   fields,
    #                   group by,
    #                   limit,
    #                   offset,
    #                   order by = ,
    #                   lazy )

    city_grouping = self.env['my.hospital'].read_group([], ['city'], ['city'])

    # search grouping ( it show like group )
    for i in city_grouping:
        print(i)

    # print(self.read(["name", "city"]))    # this will ;print all the Data [not recommeneded]

    # abc = self.env['my.hospital'].search([], limit=1)
    # print(abc.read())


# def get_hospital_count(self):
#     count = self.env["my.hospital"].search_count([('if', '>', '1')], limit=10)
#     print(f"Total Hospitals: {count}")

#     # this will show op up

#     return {
#         "type": "ir.actions.client",
#         "tag": "display_notification",
#         "params": {
#             "title": "Hospital Count",
#             "message": f"Total 'Test Hospital' records: {count}",
#             "sticky": False,
#         },
#     }

# READ GROUP
# This doesnt required records.

def get_hospital_count(self):
    count = self.env["my.hospital"].search_count([('if', '>', '1')], limit=10)
    print(f"Total Hospitals: {count}")

    # this will show op up

    return {
        "type": "ir.actions.client",
        "tag": "display_notification",
        "params": {
            "title": "Hospital Count",
            "message": f"Total 'Test Hospital' records: {count}",
            "sticky": False,
        },
    }

# class MyPatient(models.Model):
#     _name = "my.patient"
#     _description = "Patient List"
#
#     name = fields.Char(string="Name")
#     description = fields.Text(string="Description")
#
#     # def custom_method(self):
#     #     data = {
#     #         "name": "Test Hospital",
#     #         'description': 'hello',
#     #     }
#     #     self.env["my.patient"].create(data)
