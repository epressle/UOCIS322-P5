import nose
import arrow
import acp_times

def test_open():
    assert str(acp_times.open_time(300, 1000, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T09:00:00+00:00"
    assert str(acp_times.open_time(600, 1000, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T18:48:00+00:00"
    assert str(acp_times.open_time(713, 1000, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T22:50:00+00:00"
    assert str(acp_times.open_time(896, 1000, arrow.get('2010-01-01T00:00:00'))) == "2010-01-02T05:22:00+00:00"
    assert str(acp_times.open_time(1000, 1000, arrow.get('2010-01-01T00:00:00'))) == "2010-01-02T09:05:00+00:00"
    assert str(acp_times.open_time(1000, 1000, arrow.get('2010-01-03T08:05:00'))) == "2010-01-04T17:10:00+00:00"

def test_close():
    assert str(acp_times.close_time(300, 1000, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T20:00:00+00:00"
    assert str(acp_times.close_time(600, 1000, arrow.get('2010-01-01T00:00:00'))) == "2010-01-02T16:00:00+00:00"
    assert str(acp_times.close_time(713, 1000, arrow.get('2010-01-01T00:00:00'))) == "2010-01-03T01:53:00+00:00"
    assert str(acp_times.close_time(896, 1000, arrow.get('2010-01-01T00:00:00'))) == "2010-01-03T17:54:00+00:00"
    assert str(acp_times.close_time(1000, 1000, arrow.get('2010-01-01T00:00:00'))) == "2010-01-04T03:00:00+00:00"
    assert str(acp_times.close_time(1000, 1000, arrow.get('2010-01-01T23:00:00'))) == "2010-01-05T02:00:00+00:00"
