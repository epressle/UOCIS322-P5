import nose
import arrow
import acp_times

def test_open():
    assert str(acp_times.open_time(0, 600, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T00:00:00+00:00"
    assert str(acp_times.open_time(100, 600, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T02:56:00+00:00"
    assert str(acp_times.open_time(200, 600, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T05:53:00+00:00"
    assert str(acp_times.open_time(260, 600, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T07:45:00+00:00"
    assert str(acp_times.open_time(500, 600, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T15:28:00+00:00"
    assert str(acp_times.open_time(600, 600, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T18:48:00+00:00"
    assert str(acp_times.open_time(600, 600, arrow.get('2010-01-01T23:00:00'))) == "2010-01-02T17:48:00+00:00"

def test_close():
    assert str(acp_times.close_time(0, 600, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T01:00:00+00:00"
    assert str(acp_times.close_time(100, 600, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T06:40:00+00:00"
    assert str(acp_times.close_time(200, 600, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T13:20:00+00:00"
    assert str(acp_times.close_time(260, 600, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T17:20:00+00:00"
    assert str(acp_times.close_time(500, 600, arrow.get('2010-01-01T00:00:00'))) == "2010-01-02T09:20:00+00:00"
    assert str(acp_times.close_time(600, 600, arrow.get('2010-01-01T00:00:00'))) == "2010-01-02T16:00:00+00:00"
    assert str(acp_times.close_time(600, 600, arrow.get('2010-01-01T23:00:00'))) == "2010-01-03T15:00:00+00:00"
