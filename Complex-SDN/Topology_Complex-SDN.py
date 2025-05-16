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
        h5 = self.addHost( 'h5' )
        h6 = self.addHost( 'h6' )

        # Add switchs
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )

        # Add links host to switch
        self.addLink( h1, s1, 1, 1)
        self.addLink( h2, s1, 1, 2)
      
        self.addLink( h3, s2, 1, 1)
        self.addLink( h4, s2, 1, 2)
        
        self.addLink( h5, s3, 1, 1)
        self.addLink( h6, s3, 1, 2)

        # Add links switch to switch
        self.addLink( s1, s2, 4, 4)
        self.addLink( s1, s3, 3, 4)
        self.addLink( s2, s3, 3, 3)


topos = { 'mytopo': ( lambda: MyTopo() ) }
