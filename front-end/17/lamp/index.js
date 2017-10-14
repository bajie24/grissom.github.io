import Vue from 'vue'

Vue.component('buttonSwitch',{
    render: function(createElement){
        return createElement(
            'button',
            {
                on: {
                    click: this.onAndOff,
                    class: 'a b c'
                }
            },
            this.$slots.default
        )
    },
    props: ['swtichType'],
    methods: {
        onAndOff(e){
            if(!e.currentTarget.className) e.currentTarget.className = 'press';
            else e.currentTarget.className = '';
            if(e.currentTarget.textContent.indexOf('A') != (-1)){
                this.$emit('changeswitch',e.currentTarget.textContent);
                
            }else if(e.currentTarget.textContent.indexOf('B') != (-1)){
                this.$emit('changeswitch',e.currentTarget.textContent);
            }else this.$emit('changeswitch',e.currentTarget.textContent);
        }
    }
})
new Vue({
    el: '#main',
    data: {
        lightSwitch: false,
        switchA: false,
        switchB1: false,
        switchB2: false,
        switchC1: false,
        switchC2: false,
        switchC3: false,
        swtichType: ''
    },
    methods: {
        changeSwitch(e){
            if(e == 'pressA') this.switchA = !this.switchA;
            else if(e == 'pressB1') this.switchB1 = !this.switchB1;
            else if(e == 'pressB2') this.switchB2 = !this.switchB2;
            else if(e == 'pressC1') this.switchC1 = !this.switchC1;
            else if(e == 'pressC2') this.switchC2 = !this.switchC2;
            else if(e == 'pressC3') this.switchC3 = !this.switchC3;
            var isOn = this.switchA || (this.switchB1 && this.switchB2) || (this.switchC1&&this.switchC2&&this.switchC3);
            if(isOn) this.lightSwitch = true;
            else this.lightSwitch = false;
        }
    },
    watch: {
        lightSwitch(){
            if(this.lightSwitch) document.querySelector('.lamp').className='lamp light';
            else document.querySelector('.lamp').className='lamp';
        }
    }
})