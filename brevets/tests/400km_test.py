import nose
import arrow
import acp_times

def test_open():
    assert str(acp_times.open_time(0, 400, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T00:00:00+00:00"
    assert str(acp_times.open_time(20, 400, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T00:35:00+00:00"
    assert str(acp_times.open_time(40, 400, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T01:11:00+00:00"
    assert str(acp_times.open_time(120, 400, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T03:32:00+00:00"
    assert str(acp_times.open_time(194, 400, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T05:42:00+00:00"
    assert str(acp_times.open_time(400, 400, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T12:08:00+00:00"
    assert str(acp_times.open_time(400, 400, arrow.get('2010-01-01T23:00:00'))) == "2010-01-02T11:08:00+00:00"

def test_close():
    assert str(acp_times.close_time(0, 400, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T01:00:00+00:00"
    assert str(acp_times.close_time(20, 400, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T02:00:00+00:00"
    assert str(acp_times.close_time(40, 400, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T03:00:00+00:00"
    assert str(acp_times.close_time(120, 400, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T08:00:00+00:00"
    assert str(acp_times.close_time(194, 400, arrow.get('2010-01-01T00:00:00'))) == "2010-01-01T12:56:00+00:00"
    assert str(acp_times.close_time(400, 400, arrow.get('2010-01-01T00:00:00'))) == "2010-01-02T03:00:00+00:00"
    assert str(acp_times.close_time(400, 400, arrow.get('2010-01-01T23:00:00'))) == "2010-01-03T02:00:00+00:00"
