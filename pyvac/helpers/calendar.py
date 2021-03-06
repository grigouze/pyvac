import logging
import caldav
from dateutil.relativedelta import relativedelta

log = logging.getLogger(__file__)


def addToCal(url, date_from, date_end, summary):
    """ Add entry in calendar to period date_from, date_end """

    vcal_entry = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:Pyvac Calendar
BEGIN:VEVENT
SUMMARY:%s
DTSTART;VALUE=DATE:%s
DTEND;VALUE=DATE:%s
END:VEVENT
END:VCALENDAR
"""

    client = caldav.DAVClient(url)
    principal = caldav.Principal(client, url)
    calendars = principal.calendars()
    if not len(calendars):
        return False

    vcal_entry = vcal_entry % (summary,
                               date_from.strftime('%Y%m%d'),
                               (date_end + relativedelta(days=1)).strftime('%Y%m%d'))
    calendar = calendars[0]
    log.info('Using calendar %r' % calendar)
    log.info('Using entry: %s' % vcal_entry)

    event = caldav.Event(client, data=vcal_entry, parent=calendar).save()
    log.info('Event %s created' % event)

    return True
