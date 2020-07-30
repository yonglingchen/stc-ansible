import sys

labserver_ip = sys.argv[1]
print(labserver_ip)



from stcrestclient import stchttp
stc = stchttp.StcHttp(labserver_ip)
sessions = stc.sessions();
if sessions is not None:
    for session in sessions:
        stc.join_session(session)
        stc.end_session()
