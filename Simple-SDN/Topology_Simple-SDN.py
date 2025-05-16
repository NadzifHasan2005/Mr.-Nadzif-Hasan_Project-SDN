from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )

        # Add switchs
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )

        # Add links host to switch
        self.addLink( h1, s1 )
        self.addLink( h2, s1 )
        self.addLink( h3, s2 )
        self.addLink( h4, s2 )

        # Add links switch to switch
        self.addLink( s1, s2 )


topos = { 'mytopo': ( lambda: MyTopo() ) }
