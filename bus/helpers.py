from django.template.loader import render_to_string


def email_customer(occupant_first_name, occupant_last_name, seat_no , bus_title):
    render_msg= render_to_string("email_emplate.html")()