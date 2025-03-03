<template>
   <div class="navbar">
      <ul>
        <li><router-link to="/home">首页</router-link></li>
        <li><router-link to="/about">AI问答</router-link></li>
        <li><router-link to="/search">知识检索</router-link></li>
        <li><router-link to="/" class="logout-button">退出登录</router-link></li>
        <!-- <li><router-link to="/login">登录|注册</router-link></li> -->
      </ul>
    </div>
    <div id="graph-chart1">
      <div style="display:flex">
        <div style="width:100%;padding-top:100px;">
          <input type="text" v-model="entity_name" placeholder="请输入实体名" style="width:40%;margin-left:400px;height: 35px;border-radius: 10px;border:none;">
          <button style="background: #007bff; color:white; border-radius: 10px;padding: 10px 20px;margin-left: 10px;  border: none;" @click="test()">
            查询</button><br><br>
        </div>
      </div>
  
      <div id="main-chart" style="width: 100%; height: 700px; ;"></div><br><br>
      <!-- <div id="main" style="width: 100%;height:400px;"></div> -->
    </div>
  </template>
  
  
  <script>
  import axios from 'axios'
  import * as echarts from 'echarts'
  export default {
    data() {
      return {
        own: [],
        entity_name: '',
  
        categories: [{
          name: '疾病',
          itemStyle: {
            color: 'rgba(255,0,0,0.7)'
          }
        }, {
          name: '药材',
          itemStyle: {
            color: 'rgba(255, 217, 102,0.7)'
          }
        }, {
          name: '功能',
          itemStyle: {
            color: 'rgba(180, 167, 214,0.7)'
          }
        }, {
          name: '主治',
          itemStyle: {
            color: 'rgba(147, 196, 125,0.7)'
          }
        }, {
          name: '性味',
          itemStyle: {
            color: 'rgba(255, 153, 0,0.7)'
          }
        },
        {
          name: '物种',
          itemStyle: {
            color: 'rgba(234, 153, 153,0.7)'
          }
        },
        {
          name: '化学成分',
          itemStyle: {
            color: 'rgba(196,234,153,0.95)'
          }
        },
        {
          name: '拼音或英文',
          itemStyle: {
            color: 'rgba(153,187,234,0.75)'
          }
        },
        {
          name: '类别',
          itemStyle: {
            color: 'rgba(227,153,234,0.75)'
          }
        },
        {
          name: '用药',
          itemStyle: {
            color: 'rgba(153,202,234,0.91)'
          }
        }],
        data: [],
        links: [],
        entity: [],
        relation: [],
      }
    },
    methods: {
      click(name) {
        //发送请求得到相应节点对应的边
        this.own.push(name)
        this.axios.get('/entitySearch/', {
          params: {
            entity_name: name
          }
        })
          .then((response) => {
            this.entity = []
            this.relation = []
            this.entity = response.data['entity']
            this.relation = response.data['relation']
  
            this.entity.forEach(newItem => {
              if (!this.data.some(item => item.id === newItem.id)) {
                // 获取第一个元素的id
                const firstItemId = this.data.length > 0 ? this.data[0].id : null;
                const firstName = this.data.length > 0 ? this.data[0].name : null;
  
                let indexToRemove = null;
  
                // 查找第一个不在own列表中的元素的索引
                for (let i = 0; i < this.data.length; i++) {
                  if (!this.own.includes(this.data[i].name)) {
                    indexToRemove = i;
                    break;
                  }
                }
  
                // 如果不存在相同 id 的数据项，则将新数据项添加到列表中
                this.data.push(newItem);
  
                if (this.data.length > 40) {
                  // 如果第一个元素的name等于选中元素的name，则删除第二个元素，否则删除第一个元素
                  if (indexToRemove !== null) {
                    // 删除第一个不在own列表中的元素
                    let deleteName = this.data[indexToRemove].name
                    this.data.splice(indexToRemove, 1);
                    this.links = this.links.filter(link => link.source !== deleteName && link.target !== deleteName);
                  } else {
                    this.data.shift();
                    this.links = this.links.filter(link => link.source !== firstItemId && link.target !== firstItemId);
                  }
                  // 删除links列表中source或target等于第一个元素id的元素
                  // this.links = this.links.filter(link => link.source !== firstItemId && link.target !== firstItemId);
                }
              }
            });
  
            this.relation.forEach(newItem => {
              this.links.push(newItem)
            });
            // 使用 JSON.stringify 将对象转换为字符串再打印
            console.log(this.data.length)
            console.log(JSON.stringify(this.data));
            console.log(JSON.stringify(this.links));
            console.log(JSON.stringify(this.own));
            this.initChart()
          })
      },
      test() {
        if (this.entity_name == '') {
          this.$message({
            message: '请输入实体名！',
            type: 'error'
          })
        } else {
          this.own.push(this.entity_name)
          this.$message({
            message: '查询成功！',
            type: 'success'
          })
          var loadingOptions = {
            fullscreen: true,
            text: '载入数据中'
          }
          const loadingInstance = this.$loading(loadingOptions)
          // this.data=[{name:'test',category:0}]
          // this.links=[]
          // alert(this.text)
          this.axios.get('/entitySearch/', {
            params: {
              entity_name: this.entity_name
            }
          })
            .then((response) => {
              loadingInstance.close()
  
              this.data = []
              this.links = []
              // console.log(response.data['entity'])
              this.data = response.data['entity']
              // console.log(this.data)
              this.links = response.data['relation']
              this.initChart()
            })
        }
      },
      // 初始化echarts
      initChart: function () {
        let myChart =  echarts.getInstanceByDom(document.getElementById("main-chart"));
        let vm = this; // 将 Vue 实例保存到变量 vm 中
        // 检查是否已经存在图表实例
        if (myChart == null) {
          // 如果不存在图表实例，则初始化图表
          console.log("bucunzai")
          myChart = echarts.init(document.getElementById('main-chart'));
        }
        // let myChart = echarts.init(document.getElementById('main-chart'))
        myChart.resize() // 自适应大小
        window.addEventListener('resize', function () {
          myChart.resize()
        })
        myChart.setOption(this.setOption())
        //定义点击事件
        myChart.on('click', function (params) {
          // 控制台打印数据的名称
          vm.click(params.name)
        });
      },
      setOption: function () {
        let option = {
          title: {
            text: ''
          },
          // 提示框
          tooltip: {
            formatter: function (x) {
              return x.data.name
            }
          },
          // 工具箱
          toolbox: {
            // 显示工具箱
            show: true,
            feature: {
              mark: {
                show: true
              },
              // 还原
              restore: {
                show: true
              },
              // 保存为图片
              saveAsImage: {
                show: true
              }
            }
          },
          animationDurationUpdate: 1500,
          animationEasingUpdate: 'quinticInOut',
          legend: [{
            data: this.categories.map(function (a) {
              return a.name
            })
          }],
          series: [
            {
              type: 'graph',
              layout: 'force',
              symbolSize: 80, // 倘若该属性不在link里，则其表示节点的大小；否则即为线两端标记的大小
              roam: true, // 鼠标缩放功能
              edgeSymbol: ['none', 'arrow'], // 关系两边的展现形式，也即图中线两端的展现形式。arrow为箭头
              legendHoverLink: true,
              label: {
                normal: {
                  show: true, // 是否显示标签
                  textStyle: {
                    fontSize: 20
                  }
                }
              },
              legend: {
                x: 'center',
                show: false
  
              },
              // focusNodeAdjacency: true, //鼠标移到节点上时突出显示结点以及邻节点和边
  
              edgeSymbolSize: [4, 10],
              draggable: true,
              edgeLabel: {
                show: true,
                fontSize: 12, // 关系（也即线）上的标签字体大小
                formatter: '{c}'
              },
  
              force: {
                repulsion: 500,
                edgeLength: 150
              },
              categories: this.categories,
  
              data: this.data,
              links: this.links,
              lineStyle: {
                color: '#333',
                opacity: 0.8,
                type: 'dotted',
                width: 2,
                curveness: 0
              }
            }
          ]
        }
        return option
      }
  
    },
    created:
      function () {
        // this.initChart()
      },
  
    mounted:
      function () {
        // this.initChart()
      }
  }
  </script>
  
  <style>
  #graph-chart1 {
    height: 900px;
    width: 100%;
    background-color:  rgb(230, 241, 250);
  }
  .navbar {
  position: fixed;
  top: 0;
  left:-10px;
  width: 100vw;
  height:80px;
  background-color:rgba(218, 235, 251, 0.497);
  z-index: 999;
}

.navbar ul {
  list-style-type: none;
  display: flex;
  justify-content: center;
}

.navbar ul li {
  position: relative;
  padding-left:50px;
  padding-top:5px;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}
.navbar a {
  text-decoration: none;
  color: black; /* 设置初始颜色 */
  padding: 8px 16px;
}

.navbar a:visited {
  color: black; /* 点击后仍保持黑色 */
}

.navbar a:hover {
  background-color:rgba(240, 248, 255, 0.599); /* 悬停时变化 */
}

.navbar a:active,
.navbar a:focus {
  color: black; /* 点击或聚焦时保持不变 */
}
.navbar ul li .logout-button {
  color: white;
  padding: 8px 16px;
  border-radius: 4px;
  transition: background-color 0.3s;
  position: relative;
  background-color: #3967ff;
  color: #fff;
  cursor: pointer;
  border: none;
}

.navbar ul li .logout-button:hover {
  background-color: #0056b3;
}
  </style>
  