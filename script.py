import sys, json, cli

if len(sys.argv) > 2:
        #shut command
        interface = sys.argv[2]
        if sys.argv[1] == "noshut":
                f = open("interfaces.json", "r")
                interfaces = json.loads(f.read())
                f.close()
                for entry in interfaces:
                        if entry["interface"] == interface:
                                entry["admin_up"] = 1
                                f = open("interfaces.json", "w")
                                f.write(json.dumps(interfaces))
                                f.close()
                                cli.clip("configure terminal; interface "+interface+"; no shutdown; end; write")
else:
        interface = sys.argv[1]
        try:
                f = open("interfaces.json", "r")
                interfaces = json.loads(f.read())
                f.close()
                for entry in interfaces:
                        if entry["interface"] == interface and entry["admin_up"] == 0:
                                cli.clip("configure terminal; interface "+interface+"; shutdown; end; write")
                        elif entry["interface"] == interface and entry["admin_up"] == 1:
                                entry["admin_up"] = 0
                                f = open("interfaces.json", "w")
                                f.write(json.dumps(interfaces))
                                f.close()
                if not any(d["interface"] == interface for d in interfaces):
                        f = open("interfaces.json", "r")
                        interfaces = json.loads(f.read())
                        f.close()
                        interfaces.append({"interface": interface, "admin_up":0})
                        f = open("interfaces.json", "w")
                        f.write(json.dumps(interfaces))
                        f.close()
                        cli.clip("configure terminal; interface "+interface+"; shutdown; end; write")


        except:
                f = open("interfaces.json", "w")
                lista = list()
                cli.clip("configure terminal; interface "+interface+"; shutdown; end; write")
                lista.append({"interface": interface, "admin_up": 0})
                f.write(json.dumps(lista))
                f.close()
