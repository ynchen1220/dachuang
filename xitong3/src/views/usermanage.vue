<template>
    <div>
      <h2 style="margin-top:0px;">用户管理</h2>
      <el-input
        v-model="username"
        placeholder="请你输入用户名"
        style="width:200px"
      ></el-input>
  
      <el-button
        type="primary"
        icon="el-icon-search"
        @click="findUser"
      >查询</el-button>
      <el-button
        type="primary"
        icon="el-icon-plus"
        @click="aUser()"
      >新增用户</el-button>
  
      <el-table
        :data="tableData.slice((currentPage-1)*pageSize,currentPage*pageSize)"
        style="width: 100%;"
      >
        <el-table-column
          prop="pk"
          label="用户名"
          min-width="25%"
        ></el-table-column>
        <el-table-column
          prop="fields.password"
          label="密码"
          min-width="25%"
        ></el-table-column>
        <el-table-column
          prop="fields.add_time"
          label="创建时间"
          min-width="25%"
        >
          <template #default="{row}">
            <span>{{ parseTime( row.fields['add_time'])}}</span>
          </template>
        </el-table-column>
        <el-table-column
          label="操作"
          min-width="25%"
        >
          <template #default="scope">
            <el-button
              size="small"
              type="primary"
              icon="el-icon-edit"
              @click="mUser(scope.row)"
            >修改</el-button>
            <el-button
              size="small"
              icon="el-icon-delete"
              @click="dUser(scope.row)"
            >删除</el-button>
          </template>
        </el-table-column>
      </el-table>
  
      <el-dialog
        title="新增用户"
        v-model="dialogVisible"
        :before-close="handleClose"
      >
        <span>用户名</span>
        <el-input
          v-model="username_add"
          placeholder="请你输入用户名"
          style="width:200px"
        ></el-input><br><br>
        <span>密&nbsp;&nbsp;&nbsp;码</span>
        <el-input
          type="password"
          v-model="password_add"
          placeholder="请你输入密码"
          style="width:200px"
        ></el-input>
  
        <template v-slot:footer>
            <span class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button
            type="primary"
            @click="addUser()"
          >确 定</el-button>
        </span>
        </template>
      </el-dialog>
  
      <el-dialog
        title="修改密码"
       v-model="dialogVisible2"
        :before-close="handleClose"
      >
        <span>用户名</span>
        <el-input
          v-model="username_mod"
          placeholder="请你输入用户名"
          style="width:200px"
          readonly="readonly"
        ></el-input><br><br>
        <span>密&nbsp;&nbsp;&nbsp;码</span>
        <el-input
          type="password"
          v-model="password_mod"
          placeholder="请你输入新密码"
          style="width:200px"
        ></el-input>
  
        <template v-slot:footer>
            <span class="dialog-footer">
          <el-button @click="dialogVisible2 = false">取 消</el-button>
          <el-button
            type="primary"
            @click="modUser()"
          >确 定</el-button>
        </span>
        </template>
      </el-dialog>
  
      <el-dialog
        title="确认删除"
       v-model="dialogVisible3"
        :before-close="handleClose"
      >
      <template v-slot:footer>
        <span class="dialog-footer">
          <el-button @click="dialogVisible3 = false">取 消</el-button>
          <el-button
            type="primary"
            @click="delUser()"
          >确 定</el-button>
        </span>
        </template>
      </el-dialog>
  
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-sizes="[5,10, 20, 50, 100]"
        :page-size="pageSize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="tableData.length"
        class="fy"
      >
      </el-pagination>
  
    </div>
  </template>
  <script>
  
  export default {
    data() {
      return {
        // 当前页
        currentPage: 1,
        // 每页多少条
        pageSize: 10,
  
        user: '', // 保存登录用户名
  
        username: '',
  
        username_add: '',
        password_add: '',
  
        username_mod: '',
        password_mod: '',
  
        username_del: '',
        password_del: '',
  
        tableData: [],
        dialogVisible: false,
  
        dialogVisible2: false,
  
        dialogVisible3: false
  
      }
    },
    methods: {
      parseTime(time, cFormat) {
        if (arguments.length === 0) {
          return null
        }
        const format = cFormat || '{y}-{m}-{d} {h}:{i}:{s}'
        let date
        if (typeof time === 'object') {
          date = time
        } else {
          if ((typeof time === 'string') && (/^[0-9]+$/.test(time))) {
            time = parseInt(time)
          }
          if ((typeof time === 'number') && (time.toString().length === 10)) {
            time = time * 1000
          }
          date = new Date(time)
        }
        const formatObj = {
          y: date.getFullYear(),
          m: date.getMonth() + 1,
          d: date.getDate(),
          h: date.getHours(),
          i: date.getMinutes(),
          s: date.getSeconds(),
          a: date.getDay()
        }
        const time_str = format.replace(/{([ymdhisa])+}/g, (result, key) => {
          const value = formatObj[key]
          // Note: getDay() returns 0 on Sunday
          if (key === 'a') { return ['日', '一', '二', '三', '四', '五', '六'][value] }
          return value.toString().padStart(2, '0')
        })
        return time_str
      },
      // 分页
      handleSizeChange(val) {
        this.pageSize = val
      },
      handleCurrentChange(val) {
        this.currentPage = val
      },
      handleClose(done) {
        this.$confirm('确定关闭吗').then(() => {
          // function(done)，done 用于关闭 Dialog
          done()
          console.info("点击右上角 'X' ，取消按钮或遮罩层时触发")
        }).catch(() => {
          console.log('点击确定时触发')
        })
      },
  
      findUser() {
        if (this.username == '') {
          this.showUser()
          this.$message({
            message: '请输入用户名！',
            type: 'error'
          })
        } else {
          var tableData_new = []
          for (var i = 0; i < this.tableData.length; i++) {
            if (this.tableData[i].pk == this.username) {
              tableData_new.push(this.tableData[i])
            }
          }
          this.tableData = tableData_new
        }
      },
      aUser() {
        this.dialogVisible = true
        this.username_add = ''
        this.password_add = ''
      },
      addUser() {
        if (this.username_add == '') {
          this.$message({
            message: '请输入用户名！',
            type: 'error'
          })
        } else if (this.password_add == '') {
          this.$message({
            message: '请输入密码！',
            type: 'error'
          })
        } else {
          // alert(this.username_add+" "+this.password_add+"\n新增成功！")
          this.axios.get('/addUser', { params: { username: this.username_add, password: this.password_add } })
            .then((response) => {
              console.log(response.data.msg)
              this.showUser()
              if (response.data.msg == 'success') {
                this.$message({
                  message: '新增成功！',
                  type: 'success'
                })
                this.dialogVisible = false
              } else {
                this.$message({
                  message: '该用户已存在！',
                  type: 'error'
                })
              }
            })
            .catch(function (error) {
              console.log(error)
            })
        }
      },
      mUser(row) {
        this.dialogVisible2 = true
        this.username_mod = row.pk
        this.password_mod = ''
      },
      modUser() {
        if (this.password_mod == '') {
          this.$message({
            message: '请输入修改后的密码！',
            type: 'error'
          })
        } else {
          // alert(row.pk+" "+row.fields['password']+"\n修改成功！")
          this.axios.get('/modUser', { params: { username: this.username_mod, password: this.password_mod } })
            .then((response) => {
              this.$message({
                message: '修改成功！',
                type: 'success'
              })
            this.showUser()
            })
            .catch(function (error) {
              console.log(error)
            })
          this.dialogVisible2 = false
        }
      },
      dUser(row) {
        this.dialogVisible3 = true
        this.username_del = row.pk
      },
      delUser() {
        // alert(row.pk+" "+row.fields['password']+"\n删除成功！")
        this.axios.get('/delUser', { params: { username: this.username_del } })
          .then((response) => {
            this.$message({
              message: '删除成功！',
              type: 'success'
             })
            this.showUser()
            this.dialogVisible3 = false
          })
          .catch(function (error) {
            console.log(error)
          })
      },
      showUser() {
        this.axios.get('/showUser')
          .then((response) => {
            console.log(response.data.list)
            this.tableData = response.data.list
          })
          .catch(function (error) {
            console.log(error)
          })
      }
    },
    mounted() {
  
    },
    created() {
      this.showUser()
    }
  }
  
  </script>
  