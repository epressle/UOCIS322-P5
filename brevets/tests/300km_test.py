import nose
import arrow
import acp_times

def test_open():
    assert str(acp_times.open_time(0, 300, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T00:00:00+00:00"
    assert str(acp_times.open_time(50, 300, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T01:28:00+00:00"
    assert str(acp_times.open_time(100, 300, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T02:56:00+00:00"
    assert str(acp_times.open_time(130, 300, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T03:49:00+00:00"
    assert str(acp_times.open_time(250, 300, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T07:27:00+00:00"
    assert str(acp_times.open_time(300, 300, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T09:00:00+00:00"
    assert str(acp_times.open_time(300, 300, arrow.get('2010-01-01T23:00:00'))) == "2010-01-02T08:00:00+00:00"

def test_close():
    assert str(acp_times.close_time(0, 300, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T01:00:00+00:00"
    assert str(acp_times.close_time(50, 300, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T03:30:00+00:00"
    assert str(acp_times.close_time(100, 300, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T06:40:00+00:00"
    assert str(acp_times.close_time(130, 300, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T08:40:00+00:00"
    assert str(acp_times.close_time(250, 300, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T16:40:00+00:00"
    assert str(acp_times.close_time(300, 300, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T20:00:00+00:00"
    assert str(acp_times.close_time(300, 300, arrow.get('2010-01-01T23:00:00'))) == "2010-01-02T19:00:00+00:00"
