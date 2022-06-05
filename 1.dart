//#define STATICCAM

float hash1( vec2 p )
{
    p  = 50.0*fract( p*0.3183099 );
    return fract( p.x*p.y*(p.x+p.y) );
}

float hash( uint n ) 
{
	n = (n << 13U) ^ n;
    n = n * (n * n * 15731U + 789221U) + 1376312589U;
    return uintBitsToFloat( (n>>9U) | 0x3f800000U ) - 1.0;
}

vec2 hash2( float n ) { return fract(sin(vec2(n,n+1.0))*vec2(43758.5453123,22578.1459123)); }

float noise( in vec2 x )
{
    ivec2 p = ivec2(floor(x));
    vec2 f = fract(x);
	f = f*f*(3.0-2.0*f);
	ivec2 uv = p.xy;
	float rgA = texelFetch( iChannel1, (uv+ivec2(0,0))&255, 0 ).x;
    float rgB = texelFetch( iChannel1, (uv+ivec2(1,0))&255, 0 ).x;
    float rgC = texelFetch( iChannel1, (uv+ivec2(0,1))&255, 0 ).x;
    float rgD = texelFetch( iChannel1, (uv+ivec2(1,1))&255, 0 ).x;
    return mix( mix( rgA, rgB, f.x ),
                mix( rgC, rgD, f.x ), f.y );
}

float noise( in vec3 x )
{
    vec3 p = floor(x);
    vec3 f = fract(x);
	f = f*f*(3.0-2.0*f);
	vec2 uv = (p.xy+vec2(37.0,17.0)*p.z) + f.xy;
	vec2 rg = textureLod( iChannel1, (uv+0.5)/256.0, 0.0).yx;
	return mix( rg.x, rg.y, f.z );
}

float fbm4( in vec3 p )
{
    float n = 0.0;
    n += 1.000*noise( p*1.0 );
    n += 0.500*noise( p*2.0 );
    n += 0.250*noise( p*4.0 );
    n += 0.125*noise( p*8.0 );
    return n;
}

float fbm6( in vec3 p )
{
    float n = 0.0;
    n += 1.00000*noise( p*1.0 );
    n += 0.50000*noise( p*2.0 );
    n += 0.25000*noise( p*4.0 );
    n += 0.12500*noise( p*8.0 );
    n += 0.06250*noise( p*16.0 );
    n += 0.03125*noise( p*32.0 );
    return n;
}

float fbm6( in vec2 p )
{
    float n = 0.0;
    n += 1.00000*noise( p*1.0 );
    n += 0.50000*noise( p*2.0 );
    n += 0.25000*noise( p*4.0 );
    n += 0.12500*noise( p*8.0 );
    n += 0.06250*noise( p*16.0 );
    n += 0.03125*noise( p*32.0 );
    return n;
}

float fbm4( in vec2 p )
{
    float n = 0.0;
    n += 1.00000*noise( p*1.0 );
    n += 0.50000*noise( p*2.0 );
    n += 0.25000*noise( p*4.0 );
    n += 0.12500*noise( p*8.0 );
    return n;
}

float ndot(vec2 a, vec2 b ) { return a.x*b.x - a.y*b.y; }

float sdRhombus( in vec2 p, in vec2 b, in float r ) 
{
    vec2 q = abs(p);
    float h = clamp( (-2.0*ndot(q,b) + ndot(b,b) )/dot(b,b), -1.0, 1.0 );
    float d = length( q - 0.5*b*vec2(1.0-h,1.0+h) );
    d *= sign( q.x*b.y + q.y*b.x - b.x*b.y );
	return d - r;
}

float usdBox( in vec3 p, in vec3 b )
{
    return length( max(abs(p)-b,0.0 ) );
}

float sdBox( vec3 p, vec3 b )
{
  vec3 d = abs(p) - b;
  return min(max(d.x,max(d.y,d.z)),0.0) + length(max(d,0.0));
}

float sdBox( float p, float b )
{
  return abs(p) - b;
}

vec2 opRepLim( in vec2 p, in float s, in vec2 lim )
{
    return p-s*clamp(round(p/s),-lim,lim);
}

vec2 opRepLim( in vec2 p, in float s, in vec2 limmin, in vec2 limmax )
{
    return p-s*clamp(round(p/s),-limmin,limmax);
}

vec4 textureGood( sampler2D sam, in vec2 uv )
{
    uv = uv*1024.0 - 0.5;
    vec2 iuv = floor(uv);
    vec2 f = fract(uv);
    f = f*f*(3.0-2.0*f);
	vec4 rg1 = textureLod( sam, (iuv+ vec2(0.5,0.5))/1024.0, 0.0 );
	vec4 rg2 = textureLod( sam, (iuv+ vec2(1.5,0.5))/1024.0, 0.0 );
	vec4 rg3 = textureLod( sam, (iuv+ vec2(0.5,1.5))/1024.0, 0.0 );
	vec4 rg4 = textureLod( sam, (iuv+ vec2(1.5,1.5))/1024.0, 0.0 );
	return mix( mix(rg1,rg2,f.x), mix(rg3,rg4,f.x), f.y );
}

#define ZERO (min(iFrame,0))

//------------


vec3 temple( in vec3 p )
{
    vec3 op = p;    
    vec3 res = vec3(-1.0,-1.0,0.5);

    p.y += 2.0;

    // bounding box
    float bbox = usdBox(p,vec3(15.0,12.0,15.0)*1.5 );
    if( bbox>5.0 ) return vec3(bbox+1.0,-1.0,0.5);
    
    
    
    
    
    
    vec3 q = p;
    
    // columns
    float d = length(q) - 0.9;
    
    
    
    

    res = vec3( d, 1.0, res.z );

    return res;
}

vec3 map( in vec3 p )
{
    vec3 res = temple(p);
    
    // floor
    float m = p.y + 7.5;
    if( m<res.x ) res = vec3( m, 2.0, 0.0 );

    return res;
}

// https://iquilezles.org/articles/normalsSDF
vec3 calcNormal( in vec3 p, in float t )
{
#if 0    
    float e = 0.001*t;

    vec2 h = vec2(1.0,-1.0)*0.5773;
    return normalize( h.xyy*map( p + h.xyy*e ).x + 
					  h.yyx*map( p + h.yyx*e ).x + 
					  h.yxy*map( p + h.yxy*e ).x + 
					  h.xxx*map( p + h.xxx*e ).x );
#else    
    // inspired by tdhooper and klems - a way to prevent the compiler from inlining map() 4 times
    vec3 n = vec3(0.0);
    for( int i=ZERO; i<4; i++ )
    {
        vec3 e = 0.5773*(2.0*vec3((((i+3)>>1)&1),((i>>1)&1),(i&1))-1.0);
        n += e*map(p+e*0.001*t).x;
    }
    return normalize(n);
#endif    
}

vec3 intersect( in vec3 ro, in vec3 rd )
{
    vec2 ma = vec2(0.0);

    vec3 res = vec3(-1.0);
    
    float tmax = 1000.0;

        
    float t = 10.0;
    for( int i=0; i<256; i++ )
    {
        vec3 pos = ro + t*rd;
        vec3 h = map( pos );
        if( h.x<(0.0001*t) || t>tmax ) break;
        t += h.x;

        ma = h.yz;
    }

    if( t<tmax )
    {
    	res = vec3(t, ma);
    }

    return res;
}

vec4 textureBox( in sampler2D tex, in vec3 pos, in vec3 nor )
{
    vec4 cx = texture( tex, pos.yz );
    vec4 cy = texture( tex, pos.xz );
    vec4 cz = texture( tex, pos.xy );
    vec3 m = nor*nor;
    return (cx*m.x + cy*m.y + cz*m.z)/(m.x+m.y+m.z);
}

float calcShadow( in vec3 ro, in vec3 rd, float k )
{
    float res = 1.0;
    
    float t = 0.01;
    for( int i=0; i<150; i++ )
    {
        vec3 pos = ro + t*rd;
        float h = map( pos ).x;
        res = min( res, k*max(h,0.0)/t );
        if( res<0.0001 ) break;
        t += clamp(h,0.01,0.5);
    }

    return res;
}

float calcOcclusion( in vec3 pos, in vec3 nor, float ra )
{
    float occ = 0.0;
    for( int i=ZERO; i<32; i++ )
    {
        float h = 0.01 + 4.0*pow(float(i)/31.0,2.0);
        vec2 an = hash2( ra + float(i)*13.1 )*vec2( 3.14159, 6.2831 );
        vec3 dir = vec3( sin(an.x)*sin(an.y), sin(an.x)*cos(an.y), cos(an.x) );
        dir *= sign( dot(dir,nor) );
        occ += clamp( 5.0*map( pos + h*dir ).x/h, -1.0, 1.0);
    }
    return clamp( occ/32.0, 0.0, 1.0 );
}


vec3 sunLig = normalize(vec3(0.7,0.1,0.4));

vec3 skyColor( in vec3 ro, in vec3 rd )
{
    vec3 col = vec3(0.3,0.4,0.5)*0.3 - 0.3*rd.y;

    col = mix( col, vec3(0.2,0.25,0.30)*0.5, exp(-30.0*rd.y) ) ;
    
    return col;
}

vec3 doBumpMap( in vec3 pos, in vec3 nor )
{
    float e = 0.002;
    float b = 0.015;
    
	float ref = fbm6( 4.0*pos );
    vec3 gra = -b*vec3( fbm6(4.0*vec3(pos.x+e, pos.y, pos.z))-ref,
                        fbm6(4.0*vec3(pos.x, pos.y+e, pos.z))-ref,
                        fbm6(4.0*vec3(pos.x, pos.y, pos.z+e))-ref )/e;
	
	vec3 tgrad = gra - nor * dot ( nor , gra );
    return normalize( nor - tgrad );
}

vec3 doBumpMapGrass( in vec2 pos, in vec3 nor, out float hei )
{
    float e = 0.002;
    float b = 0.03;
    
	float ref = fbm6( 4.0*pos );
    hei = ref;
    
    vec3 gra = -b*vec3( fbm6(4.0*vec2(pos.x+e, pos.y))-ref,
                        e,
                        fbm6(4.0*vec2(pos.x, pos.y+e))-ref )/e;
	
	vec3 tgrad = gra - nor*dot( nor, gra );
    return normalize( nor - tgrad );
}

mat3 setCamera( in vec3 ro, in vec3 ta, float cr )
{
	vec3 cw = normalize(ta-ro);
	vec3 cp = vec3(sin(cr), cos(cr),0.0);
	vec3 cu = normalize( cross(cw,cp) );
	vec3 cv = normalize( cross(cu,cw) );
    return mat3( cu, cv, cw );
}

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
	vec2 p = (2.0*fragCoord-iResolution.xy) / iResolution.y;
    
    uvec2 px = uvec2(fragCoord);
    float ran = hash( px.x + 1920U*px.y + (1920U*1080U)*uint(iFrame*0) );    
    
    #ifdef STATICCAM
    float an = -0.96;
    #else
    float an = sin(iTime*0.2)*0.5;
    #endif
    float ra = 25.0;
    float fl = 3.0;
    vec3 ta = vec3(0.0,-2.0,0.0);
    vec3 ro = ta + vec3(ra*sin(an),6.0,ra*cos(an));
    mat3 ca = setCamera( ro, ta, 0.0 );
    vec3 rd = ca * normalize( vec3(p.xy,fl));
    
    
    vec3 col = vec3(0.0);
    
    col = skyColor( ro, rd );
    
    float resT = 10000.0;
    vec3 res = intersect( ro, rd );
    if( res.y>0.0 )
    {
        float t = res.x;
        resT = t;
        vec3 pos = ro + t*rd;
        vec3 nor = calcNormal( pos, t );
        
        float fre = pow( clamp( 1.0+dot(nor,rd), 0.0, 1.0), 5.0 );
		float foc = 1.0;
        
        vec3 mate = vec3(0.2);
        vec2 mspe = vec2(0.0);
        float mbou = 0.0;
        float mter = 0.0;
        if( res.y<1.5 )
        {
            vec3 te = textureBox( iChannel0, pos*0.05, nor ).xyz;
            //mate = vec3(0.12,0.08,0.05) + 0.15*te;
            mate = vec3(0.14,0.10,0.07) + 0.1*te;
            mate *= 0.8 + 0.4*res.z;
            mate *= 1.15;            
            mspe = vec2(1.0,8.0);
            mbou = 1.0;
            
            foc = 0.7 + 0.3*smoothstep(0.4,0.7,fbm4( 3.0*pos ));

            float ho = 1.0;
            if( pos.y>-7.5 ) ho *= smoothstep( 0.0, 5.0, (pos.y+7.5)  );
            ho = mix( 0.1+ho*0.3, 1.0, clamp( 0.6 + 0.4*dot( normalize(nor.xz*vec2(0.5,1.0)), normalize(pos.xz*vec2(0.5,1.0)) ) + 1.0*nor.y*nor.y, 0.0, 1.0 ) );
            foc *= ho;
            foc *= 0.4 + 0.6*smoothstep( 2.0, 15.0, length(pos*vec3(0.5,0.25,1.0)) );
            float rdis = clamp( -0.15*max(sdRhombus( pos.yz-vec2(8.3,0.0)+vec2(2.0,0.0), vec2(2.25,8.5), 0.05 ),-(pos.y-8.3+2.0)), 0.0, 1.0 );
            if( rdis>0.0001 ) foc = 0.1 + sqrt(rdis);
			if( pos.y<5.8 ) foc *= 0.6 + 0.4*smoothstep( 0.0, 1.5, -(pos.y-5.8) );
            if( pos.y<3.4 ) foc *= 0.6 + 0.4*smoothstep( 0.0, 2.5, -(pos.y-3.4)  );

            foc *= 0.8;            
        }
        else
        {
            mate = vec3(0.1,0.1,0.1);
			float h;
            mspe = vec2(2.5,4.0);
            mter = 1.0;
        }

        float occ = 0.33 + 0.5*nor.y;
        occ = calcOcclusion(pos,nor,ran) * foc;
        
        vec3 lig = sunLig;
        vec3 ligbak = normalize(vec3(-lig.x,0.0,-lig.z));
        float dif = clamp( dot( nor, lig ), 0.0, 1.0 );
        float sha = calcShadow( pos+nor*0.001, lig, 32.0 );
              dif *= sha;
        float amb = (0.8 + 0.2*nor.y);
              amb = mix( amb, amb*(0.5+0.5*smoothstep( -8.0,-1.0,pos.y)), mbou );

        vec3 qos = pos/1.5 - vec3(0.0,1.0,0.0);

        float bak = clamp( 0.4+0.6*dot( nor, ligbak ), 0.0, 1.0 );
              bak *= 0.6 + 0.4*smoothstep( -8.0,-1.0,qos.y);
        
        vec3 hal = normalize( lig -rd );
        float spe = pow( clamp( dot(nor,hal), 0.0, 1.0), mspe.y )*(0.1+0.9*fre)*sha*(0.5+0.5*occ);

        col = vec3(0.0);
        col += amb*3.0*vec3(0.15,0.25,0.35)*occ*(1.0+mter);
        col += dif*6.0*vec3(0.90,0.55,0.35);
        col += bak*9.0*vec3(0.10,0.11,0.12)*occ*mbou;
        col += spe*6.0*mspe.x*occ;
        
        col *= mate;

        vec3 fogcol = vec3(0.2,0.25,0.30)*0.5;

        float fog = 1.0 - exp(-0.0013*t);
        col *= 1.0-0.5*fog;
        col = mix( col, fogcol, fog );
    }

    col = max( col, 0.0 );
    
    col = sqrt( col );


    fragColor = vec4( col, 1.0 );
}