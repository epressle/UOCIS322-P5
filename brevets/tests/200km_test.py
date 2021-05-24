import nose
import arrow
import acp_times

def test_open():
    assert str(acp_times.open_time(0, 200, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T00:00:00+00:00"
    assert str(acp_times.open_time(10, 200, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T00:18:00+00:00"
    assert str(acp_times.open_time(20, 200, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T00:35:00+00:00"
    assert str(acp_times.open_time(60, 200, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T01:46:00+00:00"
    assert str(acp_times.open_time(97, 200, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T02:51:00+00:00"
    assert str(acp_times.open_time(200, 200, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T05:53:00+00:00"
    assert str(acp_times.open_time(200, 200, arrow.get('2010-01-01T23:00:00'))) == "2010-01-02T04:53:00+00:00"

def test_close():
    assert str(acp_times.close_time(0, 200, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T01:00:00+00:00"
    assert str(acp_times.close_time(10, 200, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T01:30:00+00:00"
    assert str(acp_times.close_time(20, 200, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T02:00:00+00:00"
    assert str(acp_times.close_time(60, 200, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T04:00:00+00:00"
    assert str(acp_times.close_time(97, 200, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T06:28:00+00:00"
    assert str(acp_times.close_time(200, 200, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T13:30:00+00:00"
    assert str(acp_times.close_time(200, 200, arrow.get('2010-01-01T23:00:00'))) == "2010-01-02T12:30:00+00:00"
